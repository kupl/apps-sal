n = int(input())
a = [int(i) for i in input().split(' ')]
m = int(input())
b = [int(i) for i in input().split(' ')]
aa = [a[0]]
bb = [b[0]]
for i in range(1, n):
    aa.append(aa[-1] + a[i])
for i in range(1, m):
    bb.append(bb[-1] + b[i])
a1 = set(aa)
a2 = set(bb)
if sum(a) != sum(b):
    print(-1)
else:
    print(len(a1.intersection(a2)))
