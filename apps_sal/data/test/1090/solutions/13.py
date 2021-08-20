(N, K) = list(map(int, input().split()))
S = input()
cnt = 0
for i in range(N - 1):
    if S[i] != S[i + 1]:
        cnt += 1
ans = N - 1 - max(cnt - 2 * K, 0)
print(ans)
