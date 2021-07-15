for test in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = a[0]
    c = a[1]
    d = a[-1]
    if c + b > d:
        print(-1)
    else:
        print(1, 2, n)
