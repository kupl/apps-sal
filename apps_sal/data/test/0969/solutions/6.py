s, t = input(), input()
p, d = [], [[] for i in range(26)]
for i, q in enumerate(s):
    d[ord(q) - 97].append(i)
i, n = 0, len(t)
s += '+'
t += '-'
while i < n:
    q = t[i]
    a = b = c = 0
    for j in d[ord(q) - 97]:
        k = 1
        while t[i + k] == s[j + k]:
            k += 1
        if k > a:
            a, b, c = k, j + 1, 1
        k = 1
        while t[i + k] == s[j - k]:
            k += 1
        if k > a:
            a, b, c = k, j + 1, -1
    if not a:
        print(-1)
        return
    i += a
    p.append((b, b + c * a - c))
print(len(p))
for i, j in p:
    print(i, j)
