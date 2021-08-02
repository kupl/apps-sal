t = int(input())
for test in range(t):
    n = int(input())
    a = 1
    cnt = 0
    while a <= n:
        a *= 2
        cnt += 1
    print(n * (n + 1) // 2 - 2 * (2**cnt - 1))
