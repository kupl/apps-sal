def solve(n):
    su = 0
    for i in range(1, n + 1):
        m = n // i
        su += m * (2 * i + (m - 1) * i) // 2
    return su


n = int(input())
print(solve(n))
