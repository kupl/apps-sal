S = input()
ans = 0
N = len(S)
now = S[0]
for i in range(1, N):
    if now != S[i]:
        now = S[i]
        ans += 1
print(ans)
