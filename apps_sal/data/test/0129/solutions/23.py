(n, m, k, l) = list(map(int, input().split()))
if k + l > n:
    print('-1')
else:
    x = (k + l) // m
    if (k + l) % m > 0:
        x += 1
    if x * m > n:
        print('-1')
    else:
        print(x)
