n, m = [int(k) for k in input().split()]

w = []
d0, d1 = 0, 0
c = 0

for i in range(n):
    k = input()
    w.append(k)
    d0 += 1

for i in range(m):
    k = input()
    d1 += 1
    if k in w:
        c += 1

c = c % 2
if c > 0:
    if d0 >= d1:
        print("YES")
    else:
        print("NO")
else:
    if d0 > d1:
        print("YES")
    else:
        print("NO")

