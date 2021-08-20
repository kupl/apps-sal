(n, l, r, x) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()
k = 1 << n
res = 0
lst = 0
for i in range(k):
    num = 0
    cnt = 0
    fst = -1
    for j in range(n):
        if 1 << j & i != 0:
            num += a[j]
            cnt += 1
            if fst == -1:
                fst = j
            lst = j
    if cnt > 1 and a[lst] - a[fst] >= x and (num >= l) and (num <= r):
        res += 1
print(res)
