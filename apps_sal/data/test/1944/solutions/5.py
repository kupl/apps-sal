i = int(input())
l = [None] * i
y = 0
while y < i:
    l[y] = [int(x) for x in input().split()]
    y += 1
l1 = sorted(l, key=lambda x: x[0])
l2 = sorted(l, key=lambda x: x[1])
if l1 != l2:
    print('Happy Alex')
else:
    print('Poor Alex')
