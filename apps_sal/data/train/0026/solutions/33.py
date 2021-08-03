t = int(input())
for case in range(t):
    n, m = list(map(int, input().split()))
    perimeter = 2 * n + 2 * m

    inside = m * (n - 1) + n * (m - 1)
    nobs = 2 * n * m

    if (nobs > perimeter):
        print("NO")
    else:
        print("YES")
