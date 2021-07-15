N, M, X = list(map(int, input().split()))
lis = []

for i in range(N):
    CA = list(map(int, input().split()))
    lis.append(CA)

ans = 1e9
for i in range(2 ** N):
    check = [0 for i in range(M + 1)]
    for j in range(N):
        if i >> j & 1:
            for k in range(M + 1):
                check[k] += lis[j][k]
        if min(check[1:]) >= X:
            ans = min(ans, check[0])
if ans == 1e9:
    print((-1))
else:
    print(ans)

