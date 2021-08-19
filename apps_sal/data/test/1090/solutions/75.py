(N, K) = map(int, input().split())
S = input() + '.'
l = 0
ans = 0
for i in range(N):
    if S[i] != S[i + 1]:
        ans += i - l
        l = i + 1
print(min(ans + K * 2, N - 1))
