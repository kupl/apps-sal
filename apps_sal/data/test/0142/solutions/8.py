n, l = map(int, input().split())
p = list(map(int, input().split()))
d = []
d = [[p[i] / 2**i, i + 1] for i in range(n)]
d.sort(key=lambda x: x[0])
res = 10**18
q = l
curres = 0
for i in d:
    if i[1] == 1:
        curres += p[i[1] - 1] * q
        res = min(res, curres)
        break
    curb = q // 2**(i[1] - 1)
    curres += curb * p[i[1] - 1]
    res = min(res, curres + p[i[1] - 1])
    q %= 2**(i[1] - 1)
print(res)
