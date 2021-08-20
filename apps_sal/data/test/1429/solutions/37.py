(n, s) = input().split()
n = int(n)
at = [0] * (n + 1)
cg = [0] * (n + 1)
for i in range(n):
    AT = 0
    CG = 0
    if s[i] == 'A':
        AT = 1
    elif s[i] == 'T':
        AT = -1
    elif s[i] == 'C':
        CG = 1
    else:
        CG = -1
    at[i + 1] = at[i] + AT
    cg[i + 1] = cg[i] + CG
ans = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        AT = at[j] - at[i]
        CG = cg[j] - cg[i]
        if AT == 0 and CG == 0:
            ans += 1
print(ans)
