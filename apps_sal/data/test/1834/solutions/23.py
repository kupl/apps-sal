n = int(input())
a = [int(x) for x in input().split(" ")]

a = sorted(a)

odd = n % 2 == 1
l = a[:n // 2 + odd]
r = a[n // 2 + odd:]
r = r[::-1]

res = []
for i in range(n // 2):
    res.append(l[i])
    res.append(r[i])
if odd:
    res.append(l[n // 2])

print(" ".join([str(x) for x in res]))
