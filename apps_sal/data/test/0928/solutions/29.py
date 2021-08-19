(n, k, *a) = list(map(int, open(0).read().split()))
l = r = 0
s = 0
unko = 0
while l < n:
    while r < n and s < k:
        s += a[r]
        r += 1
    if s < k:
        break
    unko += n - r + 1
    s -= a[l]
    if l == r:
        r += 1
    l += 1
print(unko)
