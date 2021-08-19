l = []
i = 0
s = '1'
while i < 100002:
    l.append(s + s[::-1])
    s = int(s)
    s += 1
    i += 1
    s = str(s)
(n, m) = map(int, input().split())
p = 0
i = 0
while i < n:
    p = (p + int(l[i]) % m) % m
    i += 1
print(p)
