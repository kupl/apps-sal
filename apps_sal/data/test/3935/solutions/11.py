
n = int(input())
a = list(map(int, input().split()))

max_ = 0
ind = -1
d = {0: 0}
mark = [0] * n

for i, x in enumerate(a):
    if x % 2 == 1:
        d[0] += 1
    else:
        cnt = 0
        while x % 2 == 0:
            cnt += 1
            x //= 2

        if cnt not in d:
            d[cnt] = 0
        d[cnt] += 1
        mark[i] = cnt

for k, v in d.items():
    if v > max_:
        max_ = v
        ind = k

remove = [a[i] for i, x in enumerate(mark) if x != ind]
print(len(remove))
print(' '.join([str(x) for x in remove]))
