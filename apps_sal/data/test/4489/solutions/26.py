n = int(input())
s = []
for _ in range(n):
    s.append(str(input()))
m = int(input())
t = []
for _ in range(m):
    t.append(str(input()))
a = []
for i in s:
    if i not in a:
        a.append(i)
for i in t:
    if i not in a:
        a.append(i)
b = []
for i in a:
    x = s.count(i)
    y = t.count(i)
    b.append(x - y)
print(max(0, max(b)))
