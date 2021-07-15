n = int(input())
l = [0 for i in range(n)]
r = [0 for i in range(n)]

for i in range(n):
    [l[i], r[i]] = map(int, input().split())

l.sort()
r.sort()

res = n
for i in range(n):
    res += max(l[i], r[i])
print(res)
