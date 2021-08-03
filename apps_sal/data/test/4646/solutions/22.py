t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    nch = 0
    ch = 0
    for i in range(n):
        if a[i] % 2 == 0 and i % 2 == 1:
            ch += 1
        elif a[i] % 2 == 1 and i % 2 == 0:
            nch += 1
    if nch != ch:
        print(-1)
    else:
        print(ch)
