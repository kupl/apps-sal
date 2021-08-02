n, m = map(int, input().split())
ms = 1000000000
for i in range(n):
    a, b = map(int, input().split())
    ms = min(ms, a / b)
print("%.8f" % (ms * m))
