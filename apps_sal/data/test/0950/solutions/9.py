from itertools import permutations as perm
(n, m) = map(int, input().split())
alpha = set([chr(x) for x in range(ord('a'), ord('z') + 1)])
digits = set([str(x) for x in range(0, 10)])
symbol = set(['*', '#', '&'])
d = [[0] * 3 for i in range(n)]
for i in range(n):
    s = input()
    a = b = c = 10 ** 9
    for j in range(len(s)):
        if s[j] in alpha:
            a = min(a, j - 0, m - j)
        elif s[j] in digits:
            b = min(b, j - 0, m - j)
        elif s[j] in symbol:
            c = min(c, j - 0, m - j)
    d[i] = [a, b, c]
p = list(perm([x for x in range(n)], 3))
ans = 10 ** 10
for x in p:
    (a, b, c) = list(x)
    if a != b and b != c and (c != a):
        ans = min(ans, d[a][0] + d[b][1] + d[c][2])
print(ans)
