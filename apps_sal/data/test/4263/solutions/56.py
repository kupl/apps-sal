S = input()
L = len(S)
ans = 0
for i in range(L):
    c = 0
    for s in S[i:]:
        if s in ['A', 'C', 'G', 'T']:
            c += 1
        else:
            break
    ans = max(ans, c)

print(ans)
