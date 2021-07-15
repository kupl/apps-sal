n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]
c = 0
for i in set(s):
    d = s.count(i)-t.count(i)
    if d > c:
        c = d
print(c)
