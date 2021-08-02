n = int(input())
res = 11
for a in range(1, int(n ** 0.5) + 1):
    if n % a == 0:
        b = n // a
        f = max(len(str(a)), len(str(b)))
        res = min(f, res)

print(res)
