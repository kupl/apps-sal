import sys
sys.setrecursionlimit(1000000)

def f(n):
    if n == 1:
        return x
    elif n == 2:
        return x + min(x, y)
    else:
        if n % 2 == 0:
            return f(n // 2) + min(y, x * (n - n // 2))
        else:
            return min(f(n + 1), f(n - 1)) + x

n, x, y = map(int, input().split())

print(f(n))
