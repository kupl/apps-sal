n, m = input().split()
n, m = int(n), int(m)
l = [0] * m
s = input().split()
for i in range(n):
    l[int(s[i]) - 1] += 1
r = 0
for i in range(m):
    r += l[i]
p, q = 0, 0
for i in range(m):
    p += l[i]
    q += l[i] * (r - p)
print(q)
