# for _ in range(1):
for _ in range(int(input())):
    # a, b = map(int, input().split())
    n = int(input())
    # arr = list(map(int, input().split()))
    # s = input()
    i = 2
    g = -1
    while i * i <= n:
        if n % i == 0:
            g = n // i
            break
        i += 1
    if g == -1:
        print(1, n - 1)
    else:
        v = n // g - 1
        print(g, g * v)
