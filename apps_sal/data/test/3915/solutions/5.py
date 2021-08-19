(p, q) = map(int, input().split())
n = 1200000
s = [0] * n
t = [q] * n
for i in range(3, int(n ** 0.5) + 1, 2):
    (u, v) = (i * i, 2 * i)
    if t[i]:
        t[u::v] = [0] * ((n - u - 1) // v + 1)
for i in range(4, n, 2):
    t[i] = 0
t[0] = t[1] = 0
for i in range(1, 10):
    s[i] = p
for i in range(1, 1000):
    a = str(i)
    b = a[::-1]
    for j in '0123456789':
        c = int(a + j + b)
        if c < n:
            s[c] = p
    s[int(a + b)] = p
for i in range(n - 1):
    t[i + 1] += t[i]
for i in range(n - 1):
    s[i + 1] += s[i]
j = 0
for (i, (u, v)) in enumerate(zip(t, s)):
    if u <= v:
        j = i
print(j)
