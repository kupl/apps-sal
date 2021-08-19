(N, M) = list(map(int, input().split()))
K = []
for i in range(M):
    K.append(list(map(int, input().split())))
p = list(map(int, input().split()))
ans = 0
for i in range(1 << N):
    flg = True
    for j in range(M):
        n = 0
        for k in K[j][1:]:
            n += i >> k - 1 & 1
        if n % 2 != p[j]:
            flg = False
            break
    if flg:
        ans += 1
print(ans)
