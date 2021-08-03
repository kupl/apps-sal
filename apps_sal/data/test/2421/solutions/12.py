import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = list(map(int, input().split()))
    c1, c2, c3, c4, c5, c6 = list(map(int, input().split()))
    c1 = min(c1, c2 + c6)
    c2 = min(c2, c1 + c3)
    c3 = min(c3, c2 + c4)
    c4 = min(c4, c3 + c5)
    c5 = min(c5, c4 + c6)
    c6 = min(c6, c5 + c1)

    ans = 0
    if (m > 0):
        if (n <= 0):
            ans = (c3 * (-n)) + (c2 * m)

        else:
            if (n <= m):
                ans = (c1 * n) + (c2 * (m - n))
            else:
                ans = (c1 * m) + (c6 * (n - m))

    elif(m < 0):
        if (n <= 0):
            if (n <= m):
                ans = (c4 * (-m)) + (c3 * (-n + m))
            else:
                ans = c4 * (-n) + c5 * (n - m)
        else:
            ans = (c6 * n) + (c5 * (-m))
    else:
        if (n <= 0):
            ans = c3 * (-n)
        else:
            ans = c6 * n
    print(ans)
