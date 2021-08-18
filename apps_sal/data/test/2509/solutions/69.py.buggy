n, k = map(int, input().split())

if k == 0:
    print(n**2)
    return

res = 0
for i in range(k + 1, n + 1):
    a = n // i
    res += (i - k) * a
    b = n % i
    res += max(0, b - k + 1)

print(res)
