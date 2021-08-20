n = int(input())
l = []
l.append(0)
l.append(1)
l.append(2)
k = 2
m = 1
while k < n:
    k = k + l[m]
    m = m + 1
    l.append(k)
if k > n:
    m = m - 1
print(m)
