S = input()
N = len(S)
(s1, s2) = ('', '')
for i in range(N):
    if i % 2 == 0:
        s1 += '1'
        s2 += '0'
    else:
        s1 += '0'
        s2 += '1'
(a1, a2) = (0, 0)
for i in range(N):
    if s1[i] != S[i]:
        a1 += 1
    if s2[i] != S[i]:
        a2 += 1
ans = min(a1, a2)
print(ans)
