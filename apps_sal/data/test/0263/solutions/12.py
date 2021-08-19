n = int(input())
m = int(input())
l = []
for i in range(n):
    l.append(int(input()))
ma = max(l)
mx = ma + m
l.sort()
for i in range(n):
    m -= ma - l[i]
if m <= 0:
    mi = ma
else:
    mi = ma + m // n
    if m % n != 0:
        mi += 1
print(mi, mx)
