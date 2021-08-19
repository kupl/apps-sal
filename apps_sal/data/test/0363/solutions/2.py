n = int(input())
res = min(9, n)
for i in range(1, 10):
    res += max(min(9 * 10 ** i, n - 10 ** i + 1), 0) * (i + 1)
print(res)
