n, m = map(int, input().split())
x = m // n
if n * x < m:
    print(-1)
else:
    k = 0
    while x % 3 == 0:
        x = x // 3
        k += 1
    while x % 2 == 0:
        x = x // 2
        k += 1
    if x != 1:
        print(-1)
    else:
        print(k)
