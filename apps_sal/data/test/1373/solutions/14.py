(n, k) = map(int, input().split())


def f(n):
    return n * (n + 1) / 2


sum = 0
for i in range(k, n + 2):
    sum += f(n) - f(n - i) - f(i - 1) + 1
print(int(sum % (10 ** 9 + 7)))
