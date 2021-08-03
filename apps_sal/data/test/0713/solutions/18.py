n, m = list(map(int, input().split()))

s = min(n, m)
print(s + 1)
for x in range(s + 1):
    if n < m:
        print(x, m - x)
    else:
        print(n - x, x)
