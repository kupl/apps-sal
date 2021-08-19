(n, a, b) = list(map(int, input().split()))
n *= 6
swapped = False
if a > b:
    (a, b) = (b, a)
    swapped = True
(a, b) = (min(a, b), max(a, b))
(a1, b1) = (a, b)
s = 1 << 61
for i in range(a, int(n ** 0.5) + 1):
    j = max(b1, (n - 1) // i + 1)
    if i * j < s:
        s = i * j
        (a, b) = (i, j)
print(a * b)
if swapped:
    print(b, a)
else:
    print(a, b)
