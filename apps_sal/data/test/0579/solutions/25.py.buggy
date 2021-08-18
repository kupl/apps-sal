import sys


class SWAG:
    def __init__(self):
        self.fold_l = []
        self.r = []
        self.fold_r = ~(1 << 60)

    def push(self, a):
        if self.fold_r < a:
            self.fold_r = a
        self.r.append(a)

    def pop(self):
        if not self.fold_l:
            self.r.reverse()
            self.fold_l = self.r
            self.r = []
            self.fold_r = ~(1 << 60)
            fold_l = self.fold_l
            for i in range(len(fold_l) - 1):
                if fold_l[i + 1] < fold_l[i]:
                    fold_l[i + 1] = fold_l[i]
        self.fold_l.pop()

    def get(self):
        if not self.fold_l:
            return self.fold_r
        elif not self.r:
            return self.fold_l[-1]
        else:
            return max(self.fold_l[-1], self.fold_r)


n, k = list(map(int, input().split()))
p = [*list(map(int, input().split()))]
c = [*list(map(int, input().split()))]
for i in range(n):
    p[i] -= 1

if max(c) < 0:
    print((max(c)))
    return

ans = 0
used = [False] * n
for i in range(n):
    if used[i]:
        continue

    # ループを取り出す
    loop = []
    at = i
    while not used[at]:
        loop.append(c[at])
        used[at] = True
        at = p[at]

    siz = len(loop)
    cusum = [0] + loop * 3
    for i in range(siz * 3):
        cusum[i + 1] += cusum[i]
    sum = max(0, cusum[siz])

    # k % siz 回以下での最大 -> 累積和にスライド最大値
    d = k % siz
    swag = SWAG()
    for i in range(d):
        swag.push(cusum[i])
    for i in range(siz):
        swag.push(cusum[d + i])
        ans = max(ans, swag.get() - cusum[i] + sum * (k // siz))
        swag.pop()

    if k < siz:
        continue

    # k % siz + siz 回以下での最大
    d = k % siz + siz
    swag = SWAG()
    for i in range(d):
        swag.push(cusum[i])
    for i in range(siz):
        swag.push(cusum[d + i])
        ans = max(ans, swag.get() - cusum[i] + sum * (k // siz - 1))
        swag.pop()

print(ans)
