n = int(input())
f = 0

for p in range(63):
    N = 1 << (p + 1)
    l = 0
    h = n
    while h >= l:
        m = (l + h) // 2
        x = m * 2 + 1
        res = x * (x + N - 3)
        if res == n * 2:
            print(x * (1 << p))
            f = 1
            break
        elif res > n * 2:
            h = m - 1
        else:
            l = m + 1

if f == 0:
    print(-1)
