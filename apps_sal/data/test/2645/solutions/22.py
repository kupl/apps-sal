p = 0
g = 0
S = list(input())
ans = 0
for i in range(len(S)):
    if S[i] == "g" and p < g:
        ans += 1
        p += 1
    elif S[i] == "g" and p == g:
        g += 1
    if S[i] == "p" and p < g:
        p += 1
    elif S[i] == "p" and p == g:
        ans -= 1
        g += 1
print(ans)
