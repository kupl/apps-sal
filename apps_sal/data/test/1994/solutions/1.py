s = ' ' + input()
n = len(s)
r, c = [-1] * n, [1] * n
for i in range(1, n):
    r[i] = r[i - 1] + 1
    while r[i] and s[r[i]] != s[i]:
        r[i] = r[r[i] - 1] + 1
d, n = [], n - 1
for i in range(n, 1, -1):
    c[r[i]] += c[i]
while n > 0:
    d.append(str(n) + ' ' + str(c[n]))
    n = r[n]
print(len(d))
d.reverse()
print('\n'.join(d))
