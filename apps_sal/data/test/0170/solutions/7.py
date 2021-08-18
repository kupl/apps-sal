
n = int(input())
l1 = [int(i) for i in input().split()]
k1 = l1.pop(0)
l1.reverse()
l2 = [int(i) for i in input().split()]
k2 = l2.pop(0)
l2.reverse()
i = 0
dup = set()
while len(l1) > 0 and len(l2) > 0:
    c = tuple(l1 + [0.5] + l2)
    if c in dup:
        break
    dup.add(c)
    a = l1.pop()
    b = l2.pop()
    if a > b:
        l1.insert(0, b)
        l1.insert(0, a)
    else:
        l2.insert(0, a)
        l2.insert(0, b)
    i += 1
if len(l1) == 0:
    print(i, 2)
elif len(l2) == 0:
    print(i, 1)
else:
    print(-1)
