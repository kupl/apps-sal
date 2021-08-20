(n, m) = map(int, input().split())
a = 2 * n
b = 3 * m
i = 6
while i <= min(a, b):
    if b < a:
        b += 3
    else:
        a += 2
    i += 6
print(max(a, b))
