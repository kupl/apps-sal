def solve():
    n = int(input())
    a = list(map(int, input().split()))
    (p0, p1, p2) = (0, 0, 0)
    for el in a:
        if el % 3 == 0:
            p0 += 1
        elif el % 3 == 1:
            p1 += 1
        else:
            p2 += 1
    return p0 + min(p1, p2) + (max(p1, p2) - min(p1, p2)) // 3


q = int(input())
for i in range(q):
    print(solve())
