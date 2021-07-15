n = int(input())
a = [input() for i in range(n)]
m = int(input())
b = [input() for i in range(m)]
s = a + b
t = []
for i in s:
  t.append(a.count(i) - b.count(i))
  
print((0 if max(t) <= 0 else max(t)))

