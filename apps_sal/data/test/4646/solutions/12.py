for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    d = 0
    for i in range(n):
        if a[i] % 2 != i % 2:
            if a[i] % 2 == 1:
                c += 1
            else:
                d += 1
    if c == d:
        print(c)
    else:
        print(-1)
