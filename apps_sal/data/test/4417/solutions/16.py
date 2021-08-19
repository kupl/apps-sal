for i in range(int(input())):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    (b, c) = (a[0], a[-1])
    if c - b > k * 2:
        print(-1)
    else:
        print(b + k)
