for _ in range(int(input())):
    k = int(input())
    a = [int(x) for x in input().split()]
    m = sum(a)
    y = k % m
    if y == 0:
        y = m
    x = (k - y) // m
    a1 = a + a
    ml = 100
    for i in range(14):
        s = 0
        for j in range(i, 14):
            s += a1[j]
            if s == y:
                ml = min(ml, j - i + 1)

    ans = 7 * x + ml
    print(ans)
