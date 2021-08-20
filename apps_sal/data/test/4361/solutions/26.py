(N, K) = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = sorted(A)
ans = []
for i in range(N - K + 1):
    ans.append(B[i + K - 1] - B[i])
print(min(ans))
