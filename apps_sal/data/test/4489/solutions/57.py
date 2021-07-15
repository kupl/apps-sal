n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
a = 0
for x in set(s):
  a = max(s.count(x) - t.count(x), a)
print(a)
