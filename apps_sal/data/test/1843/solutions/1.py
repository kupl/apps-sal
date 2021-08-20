T = int(input())
for cas in range(T):
    n = int(input())
    res = n * (n + 1) // 2
    for i in range(40):
        if 1 << i > n:
            break
        else:
            res -= 2 * (1 << i)
    print(res)
