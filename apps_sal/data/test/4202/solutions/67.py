(L, R) = map(int, input().split())
p = 2019
if R - L >= p:
    print(0)
else:
    res = p
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            res = min(res, i * j % p)
    print(res)
