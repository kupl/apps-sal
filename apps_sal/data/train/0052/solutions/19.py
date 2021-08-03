n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
r = l[:]
r.reverse()
res = 0
for i in range(n):
    res = (res + l[i] * r[i]) % 10007
print(res)
