from math import ceil


def is_ok(m):
    tmp = h[:]
    for i in range(N):
        tmp[i] -= m * B
    flag = True
    for i in tmp:
        if i > 0:
            flag = False
            break
    if flag:
        return True
    else:
        rem = 0
        for i in tmp:
            if i > 0:
                rem += ceil(i / (A - B))
        if rem > m:
            return False
        return True


(N, A, B) = map(int, input().split())
h = list((int(input()) for _ in range(N)))
s = sum(h)
r = 10 ** 10
l = 0
while abs(l - r) > 1:
    m = (r + l) // 2
    if is_ok(m):
        r = m
    else:
        l = m
print(r)
