S = list(input())
T = list(input())

ans = 0
for i in range(len(S)):
    s = S[i:]
    if len(s) < len(T):
        break
    tmp = 0
    for j in range(len(T)):
        if s[j] == T[j]:
            tmp += 1
    ans = max(ans, tmp)

print(len(T) - ans)
