for i in range(int(input())):
    a, b, x, y, n = list(map(int, input().split()))

    a1, b1, x1, y1, n1 = a, b, x, y, n
    toRemove = min(a1 - x1, n1)
    n1 -= toRemove
    a1 -= toRemove
    toRemove = min(n1, b1 - y1)
    n1 -= toRemove
    b1 -= toRemove
    ans1 = a1 * b1

    a1, b1, x1, y1, n1 = a, b, x, y, n
    toRemove = min(b1 - y1, n1)
    n1 -= toRemove
    b1 -= toRemove
    toRemove = min(n1, a1 - x1)
    n1 -= toRemove
    a1 -= toRemove
    ans2 = a1 * b1

    print(min(ans1, ans2))
