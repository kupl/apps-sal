(n, m) = list(map(int, input().split()))
(a, b, i) = (2 * n, 3 * m, 6)
while i <= min(a, b):
    if b < a:
        b += 3
    else:
        a += 2
    i += 6
print(max(a, b))
