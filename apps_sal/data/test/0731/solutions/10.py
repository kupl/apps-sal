(w, m, k) = list(map(int, input().split()))
n = m - 1
l = len(str(m))
while w > 0:
    t = (10 ** l - n - 1) * l * k
    if w <= t:
        n += w // (l * k)
        w = 0
    else:
        n = 10 ** l
        w = w - t - (l + 1) * k
        l += 1
print(n - m + 1)
