s = input()
n = len(s)
if n == 1:
    print('1\n1 1\n')
    return
p = [-1] * n
q = -1
for i in range(1, n):
    while q >= 0 and s[i] != s[q + 1]:
        q = p[q]
    if s[i] == s[q + 1]:
        q += 1
        p[i] = q
# print(p)
c = [1] * n
for i in range(n - 1, -1, -1):
    if p[i] >= 0:
        c[p[i]] += c[i]
# print(c)
ans = [(n, 1)]
q = p[n - 1]
while q >= 0:
    ans.append((q + 1, c[q]))
    q = p[q]
print(len(ans))
print('\n'.join([' '.join(map(str, x)) for x in reversed(ans)]))
