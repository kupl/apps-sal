n, a, b = map(int, input().split())
ns = n % (a + b)
# print(ns)
if a == 0:
    print(0)
else:
    print(1 * min(ns, a) + a * (n // (a + b)))
