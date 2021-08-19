N = int(input())
A = list(map(int, input().split()))
s = [0] * (N + 1)
for i in range(N - 1):
    s[i + 1] = s[i] + A[i]
ans = 10 ** 10
for i in range(1, N):
    diff = abs(s[N - 1] + A[-1] - s[i] - s[i])
    ans = min(ans, diff)
print(ans)
