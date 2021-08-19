q = int(input())
for t in range(q):
    (l1, r1, l2, r2) = [int(a) for a in input().split()]
    if l1 == l2:
        print(l1, r2)
    else:
        print(l1, l2)
