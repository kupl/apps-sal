n = int(input())
for i in range(n):
    (l1, r1, l2, r2) = list(map(int, input().split()))
    x1 = l1
    x2 = l2
    if x1 == x2:
        if x1 + 1 < l1:
            x1 = x1 + 1
        else:
            x2 = x2 + 1
    print(x1, x2)
