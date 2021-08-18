n = int(input())

ans = 0
def g(x): return (x * (n // x) * (n // x + 1)) // 2


print((sum(g(i) for i in range(1, n + 1))))
