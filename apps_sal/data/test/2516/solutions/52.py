from collections import Counter
(n, p) = list(map(int, input().split()))
s = input()
a = 0
t = list(map(int, list(s)))
t.reverse()
if p == 2:
    for i in range(n):
        if t[i] % 2 == 0:
            a += len(t) - i
elif p == 5:
    for i in range(n):
        if t[i] % 5 == 0:
            a += len(t) - i
else:
    u = []
    k = 1
    l = 0
    for i in t:
        l = (l + i * k) % p
        u.append(l)
        k = k * 10 % p
    c = Counter(u)
    a += c[0]
    for i in list(c.values()):
        if i > 1:
            a += i * (i - 1) // 2
print(a)
