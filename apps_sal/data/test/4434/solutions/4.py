for _ in range(int(input())):
    n = int(input())
    x = n // 2
    res = 0
    for i in range(1, x + 1):
        res += 8 * i * i
    print(res)
