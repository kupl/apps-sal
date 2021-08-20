(a, b) = list(map(int, input().split()))
c = b % a == 0
if c:
    z = 0
    x = b // a
    while x % 2 == 0:
        x //= 2
        z += 1
    while x % 3 == 0:
        x //= 3
        z += 1
    if x == 1:
        print(z)
    else:
        print(-1)
else:
    print(-1)
