N, K = map(int, input().split())
S = input()
a = 0
for i in range(N - 1):
    if S[i] != S[i+1]:
        a += 1
ans = N - 1 - max(0, a - (2 * K))
print(ans)
