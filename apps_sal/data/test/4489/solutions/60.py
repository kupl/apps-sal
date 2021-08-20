n = int(input())
s = list((input() for i in range(n)))
m = int(input())
t = list((input() for i in range(m)))
r = list(set(s + t))
ans = 0
for i in r:
    a = s.count(i)
    b = t.count(i)
    ans = max(ans, a - b)
print(ans)
