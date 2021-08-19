def I():
    return list(map(int, input().split()))


(n, m) = I()
(l, r) = I()
min_length = r - l + 1
for _ in range(m - 1):
    (l, r) = I()
    min_length = min(r - l + 1, min_length)
print(min_length)
print(' '.join(([str(x) for x in range(min_length)] * (n // min_length + 1))[:n]))
