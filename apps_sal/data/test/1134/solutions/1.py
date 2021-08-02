def read_data():
    n = int(input().strip())
    a = list(map(int, list(input().strip().split())))
    return n, a


def solve():
    under = [0 for i in range(n)]
    under[-1] = a[-1] + 1
    for i in range(n - 2, -1, -1):
        under[i] = max(a[i] + 1, a[i + 1], under[i + 1] - 1)
    for i in range(1, n):
        under[i] = max(under[i], under[i - 1])
    return sum(under[i] - 1 - a[i] for i in range(n))


n, a = read_data()
print(solve())
