t = int(input())
for _ in range(t):
    (n, x) = map(int, input().split())
    a = list(map(int, input().split()))
    f = True
    g = False
    s = 0
    for i in range(n):
        if a[i] == x:
            g = True
        if a[i] != x:
            f = False
        s += a[i] - x
    if f:
        print(0)
    elif s == 0:
        print(1)
    elif g:
        print(1)
    else:
        print(2)
