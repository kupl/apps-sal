N, K = list(map(int, input().split()))
S = input()
ans = 0
for i in range(1, N):
    if S[i] == S[i - 1]:
        ans += 1

print((min(N - 1, ans + 2 * K)))
