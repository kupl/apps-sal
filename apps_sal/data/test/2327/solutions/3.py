t = int(input())
for i in range(t):
    (n, k, s) = (int(input()), 1, 0)
    while n > 0:
        (n, k, s) = (n // 2, k + 1, s + (n + 1) // 2 * k)
    print(s)
