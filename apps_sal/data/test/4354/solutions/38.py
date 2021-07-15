N, M = list(map(int, input().split()))

P = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    P.append([a, b])

C = []
for _ in range(M):
    c, d = list(map(int, input().split()))
    C.append([c, d])

for i in range(N):
    ans = float('inf')
    num = float('inf')
    for j in range(M):
        if num > abs(P[i][0] - C[j][0]) + abs(P[i][1] - C[j][1]):
            num = abs(P[i][0] - C[j][0]) + abs(P[i][1] - C[j][1])
            ans = j + 1

    print(ans)

