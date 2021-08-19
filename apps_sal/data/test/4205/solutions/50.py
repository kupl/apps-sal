N = int(input())
p = list(map(int, input().split()))
res = False
for i in range(N):
    for j in range(i, N):
        flg = True
        (p[i], p[j]) = (p[j], p[i])
        for k in range(N - 1):
            if p[k] > p[k + 1]:
                flg = False
        if flg:
            res = True
            break
        (p[i], p[j]) = (p[j], p[i])
print(['NO', 'YES'][res])
