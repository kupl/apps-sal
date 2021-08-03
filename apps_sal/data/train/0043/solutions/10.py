def xxx(x):
    nonlocal a, b
    res = 0
    for i in range(len(a)):
        if a[i] > x:
            res += b[i]
    if res <= x:
        return True
    else:
        return False


for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    i1 = 0
    i2 = sum(b)
    while i2 - i1 > 1:
        m = (i1 + i2) // 2
        if xxx(m):
            i2 = m
        else:
            i1 = m
    print(i2)
