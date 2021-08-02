n = int(input())
s = []
t = []
ans = 0
for i in range(n):
    s.append(input())
m = int(input())
for i in range(m):
    t.append(input())
l = set(s)
for i in l:
    ans = max(ans, s.count(i) - t.count(i))
print(ans)
