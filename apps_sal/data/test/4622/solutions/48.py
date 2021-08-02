n = int(input())
a = [int(x) for x in input().split()]
c = []
res = "YES"
for i in range(n):
    c.append(a[i])
c = set(c)
if len(c) != n:
    res = "NO"
print(res)
