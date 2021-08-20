(n, a, b) = list(map(int, input().split()))


def sum_digit(x):
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s


print(sum([i for i in range(1, n + 1) if a <= sum_digit(i) <= b]))
