S = input()
ans = 0
for i in range(0, len(S) // 2):
    if S[i] != S[len(S) - 1 - i]:
        ans += 1
print(ans)
