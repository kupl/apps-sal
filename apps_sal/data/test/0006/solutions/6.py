t = int(input())
for i in range(t):
    (n, x) = (int(i) for i in input().split())
    mr = 0
    md = 0
    for j in range(n):
        (d, h) = (int(i) for i in input().split())
        md = max(d, md)
        mr = max(d - h, mr)
    x -= md
    if not mr and x > 0:
        print(-1)
    elif x <= 0:
        print(1)
    else:
        f = x // mr + 1
        if x % mr:
            f += 1
        print(f)
