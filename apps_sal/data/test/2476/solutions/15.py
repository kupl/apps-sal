N = int(input())
A = list(map(int, input().split()))
C = [0] * N
D = [0] * (N + 1)
for a in A:
    C[a - 1] += 1
    D[C[a - 1]] += 1
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + D[i + 1]
ans = N
for K in range(1, N + 1):
    while ans > 0 and S[ans] < K * ans:
        ans -= 1
    print(ans)
