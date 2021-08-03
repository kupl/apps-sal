n, h, *A = list(map(int, open(0).read().split()))
a = max(A[::2])
b = sorted(A[1::2])[::-1]
for i in range(n):
    if h <= 0:
        n = i
        h = 0
        break
    if b[i] < a:
        n = i
        break
    h -= b[i]
print((n - (-h // a)))
