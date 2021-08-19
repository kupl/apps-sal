def comb(n, r):
    if n < r:
        return 0
    ret = 1
    for i in range(1, r + 1):
        ret = ret * (n - i + 1) // i
    return ret


(n, a, b) = list(map(int, input().split()))
v = list(map(int, input().split()))
v.sort(reverse=True)
ave = sum(v[:a]) / a
if v[0] == v[a - 1]:
    sm = v.count(v[0])
    cnt = 0
    for i in range(a, b + 1):
        cnt += comb(sm, i)
else:
    last = v[a - 1]
    select = v[:a].count(last)
    sm = v.count(last)
    cnt = comb(sm, select)
print(ave)
print(cnt)
