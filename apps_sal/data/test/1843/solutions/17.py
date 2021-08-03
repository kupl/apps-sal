t = int(input())
for i in range(t):
    n = int(input())
    summ = (n + 1) * (n // 2)
    if (n % 2 != 0):
        summ += (n + 1) // 2
    x = 1
    while x <= n:
        summ -= 2 * x
        x *= 2
    print(summ)
