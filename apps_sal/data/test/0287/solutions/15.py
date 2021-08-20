(n, k) = map(int, input().split())
if k == n or k == 0:
    a = 0
else:
    a = 1
b = 0
if n == k or k == 0:
    b = 0
else:
    b = min(n // 3, k) * 2
    k -= min(n // 3, k)
    if k != 0:
        if n % 3 == 1:
            k -= 1
        elif n % 3 == 2:
            k -= 1
            b += 1
    b -= k
print(a, b)
