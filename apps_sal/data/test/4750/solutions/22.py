q = int(input())
for i in range(q):
    l1, r1, l2, r2 = list(map(int, input().split()))
    if l1 < l2:
        print(l1, r2)
    else:
        print(r1, l2)
