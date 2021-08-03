n = int(input())
s = []
t = []
for i in range(n):
    s.append(input())
m = int(input())
for i in range(m):
    t.append(input())

m = 0
for i in range(n):
    x = s.count(s[i]) - t.count(s[i])
    m = max(m, x)

print(m)
