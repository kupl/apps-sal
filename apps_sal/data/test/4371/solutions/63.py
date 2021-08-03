S = input()
ans = 999
for i in range(len(S) - 2):
    s = S[i] + S[i + 1] + S[i + 2]
    ans = min(ans, abs(753 - int(s)))

print(ans)
