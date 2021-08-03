S = str(input())

N = len(S)
half = (N + 1) // 2
ans = 0
for i in range(half):
    if S[i] != S[N - 1 - i]:
        ans += 1
print(ans)
