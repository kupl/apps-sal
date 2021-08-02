for _ in [0] * int(input()):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(0, n, 2):
        print(-a[i + 1], a[i], end=' ')
    print()
