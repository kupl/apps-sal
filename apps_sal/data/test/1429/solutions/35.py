(_, S) = input().split()
N = len(S)
ans = 0
for i in range(0, N - 1):
    AT = 0
    CG = 0
    if S[i] == 'A':
        AT += 1
    elif S[i] == 'T':
        AT -= 1
    elif S[i] == 'C':
        CG += 1
    elif S[i] == 'G':
        CG -= 1
    for j in range(i + 1, N):
        if S[j] == 'A':
            AT += 1
        elif S[j] == 'T':
            AT -= 1
        elif S[j] == 'C':
            CG += 1
        elif S[j] == 'G':
            CG -= 1
        if AT == 0 and CG == 0:
            ans += 1
print(ans)
