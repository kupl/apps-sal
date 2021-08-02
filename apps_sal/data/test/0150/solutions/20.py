def prime(x):
    y = min(x, int(x ** 0.5) + 2)
    for d in range(2, y):
        if x % d == 0:
            return False
    return True


def solve(n):
    if prime(n):
        return 1
    if n % 2 and prime(n - 2):
        return 2
    return 2 + n % 2


n = int(input())
print(solve(n))
