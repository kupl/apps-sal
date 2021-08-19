t = int(input())
for _ in range(t):
    (n,) = map(int, input().split())
    x = n
    s = 0
    while x != 1 and x % 3 == 0:
        if x % 6 == 0:
            x //= 6
            s += 1
        else:
            x *= 2
            s += 1
    if x == 1:
        print(s)
    else:
        print(-1)
