def solve(n):
    x = n // 3
    c = 2 * x
    n -= 3 * x
    if n:
        c += 1
    return c

n = int(input())

print(solve(n))

