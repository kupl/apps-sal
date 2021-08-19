T = int(input())
for test in range(T):
    (a, b, n) = list(map(int, input().split(' ')))
    res = 0
    while a <= n and b <= n:
        res += 1
        if a < b:
            a += b
        else:
            b += a
    print(res)
