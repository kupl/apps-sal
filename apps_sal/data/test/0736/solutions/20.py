(n, m) = list(map(int, input().split()))
if n % 2 == 0:
    a = n // 2
    b = n // 2 * 2
if n % 2 != 0:
    a = n // 2 + 1
    b = n // 2 * 2 + 1
o = -1
for i in range(a, b + 1):
    if i % m == 0:
        o = i
        break
print(o)
