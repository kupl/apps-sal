R = lambda: list(map(int, input().split()))
n, k, x = R()
a = list(R())
print(sum(a[:n - k]) + k * x)
