n = int(input())
s = set()
for i in range(1, 32):
    s.add(i ** 2)
for i in range(1, 11):
    s.add(i ** 3)
for i in range(1, 7):
    s.add(i ** 4)
for i in range(1, 5):
    s.add(i ** 5)
    s.add(i ** 6)
    s.add(i ** 7)
    s.add(i ** 8)
    s.add(i ** 9)
    s.add(i ** 10)
t = list(s)
t.sort()
t = [x for x in t if x <= 1000]
res = 0
for tt in t:
    res = tt if tt <= n else res
print(res)
