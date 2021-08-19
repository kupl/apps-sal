for _ in range(int(input())):
    (n, a, b, c, d) = list(map(int, input().split()))
    if (a - b) * n <= c + d and (a + b) * n >= c - d:
        print('Yes')
    else:
        print('No')
