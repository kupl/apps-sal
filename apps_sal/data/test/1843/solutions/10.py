for t in range(int(input())):
    n = int(input())
    (v, p2) = (n * (n + 1) // 2, 1)
    while p2 <= n:
        v -= 2 * p2
        p2 *= 2
    print(v)
