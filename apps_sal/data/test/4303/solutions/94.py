(n, k) = map(int, input().split())
x = list(map(int, input().split()))
c = 10 ** 9
for i in range(n - k + 1):
    a = x[i + k - 1]
    b = x[i]
    if a < 0:
        c = min(c, abs(b))
    elif b < 0:
        c = min(c, min(a, abs(b)) * 2 + max(a, abs(b)))
    else:
        c = min(c, a)
print(c)
