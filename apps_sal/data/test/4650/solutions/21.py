t = int(input())
for i in range(t):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    (ost0, ost1, ost2) = (0, 0, 0)
    col = 0
    for el in a:
        if el % 3 == 0:
            ost0 += 1
        elif el % 3 == 1:
            ost1 += 1
        elif el % 3 == 2:
            ost2 += 1
    col += ost0 + min(ost1, ost2) + (max(ost1, ost2) - min(ost1, ost2)) // 3
    print(col)
