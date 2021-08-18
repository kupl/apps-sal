
try:
    while True:
        n, p = list(map(int, input().split()))
        a = [0] * n
        for i in range(n):
            lower, upper = list(map(int, input().split()))
            a[i] = (upper // p - (lower - 1) // p) / (upper - lower + 1)
        print(sum(a[i] + (1 - a[i]) * a[i - 1] for i in range(n)) * 2000)

except EOFError:
    pass
