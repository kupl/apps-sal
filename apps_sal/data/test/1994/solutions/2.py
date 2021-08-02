s = input()
n = len(s)
p = [0]
for i in range(1, n):
    j = p[i - 1]
    while j > 0 and s[j] != s[i]:
        j = p[j - 1]
    if s[j] == s[i]:
        j += 1
    p.append(j)
a = []
k = n
while k != 0:
    a += [k]
    k = p[k - 1]
c = [0] * (n + 1)
for i in range(n):
    c[p[i]] += 1
for i in range(n - 1, 1, -1):
    c[p[i - 1]] += c[i]
print(len(a))
for t in a[::-1]:
    print(t, c[t] + 1)
