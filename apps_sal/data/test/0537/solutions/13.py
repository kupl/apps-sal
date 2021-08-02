n, k = map(int, input().split())

l = -1
r = n

while r - l > 1:
    m = (l + r) // 2
    if (m + m * k > n // 2):
        r = m
    else:
        l = m

print(l, l * k, n - l - l * k)
