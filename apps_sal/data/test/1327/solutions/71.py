N, M = map(int, input().split())
C = [tuple(map(int, input().split())) for _ in range(N)]
 
res = 0
 
for i in range(8): # x, y, z を正にするか負にするか8通り試す
    D = [0 for _ in range(N)]
    for j in range(N):
        x, y, z = C[j]
        if (i >> 0) & 1:
            D[j] += x
        else:
            D[j] -= x
        if (i >> 1) & 1:
            D[j] += y
        else:
            D[j] -= y
        if (i >> 2) & 1:
            D[j] += z
        else:
            D[j] -= z
    D.sort(reverse=True)
    res = max(res, sum(D[:M])) # その中で一番大きいものM個をとる
 
print(res)
