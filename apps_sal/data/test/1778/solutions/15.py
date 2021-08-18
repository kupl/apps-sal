n = int(input())
l1 = list(sorted(map(int, input().split())))
l2 = list(sorted(map(int, input().split())))
s1 = s2 = 0
while len(l1) > 0 or len(l2) > 0:
    k1 = k2 = 0
    if len(l1) > 0:
        k1 = l1[-1]
    if len(l2) > 0:
        k2 = l2[-1]
    if k1 >= k2:
        s1 += k1
        l1.pop()
    else:
        l2.pop()
    if len(l1) == 0 and len(l2) == 0:
        break
    k1 = k2 = 0
    if len(l1) > 0:
        k1 = l1[-1]
    if len(l2) > 0:
        k2 = l2[-1]
    if k2 >= k1:
        s2 += k2
        l2.pop()
    else:
        l1.pop()
print(s1 - s2)
