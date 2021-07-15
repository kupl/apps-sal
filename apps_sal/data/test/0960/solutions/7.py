n, k = map(int, input().split())
minn = 10 ** 9
for m in range(1, k):
    if n % m == 0:
        if minn > (n // m) * k + m:
            minn = (n // m) * k + m
print(minn)
