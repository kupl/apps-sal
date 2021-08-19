n = int(input())
(s, p) = ({}, [''] * n)
for k in range(n):
    p[k] = input()
    for q in [p[k][i:j] for i in range(9) for j in range(i + 1, 10)]:
        s[q] = -1 if q in s and s[q] != k else k
for (q, k) in list(s.items()):
    if ~k and len(p[k]) > len(q):
        p[k] = q
print('\n'.join(p))
