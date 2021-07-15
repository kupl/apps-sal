N, Q, *QX = map(int, open(0).read().split())

A = [N] * (N + 1)
B = [N] * (N + 1)

ans = (N - 2) ** 2
h = w = N
for q, x in zip(*[iter(QX)] * 2):
    if q == 1:
        if x < w:
            B[x:w] = [h] * (w - x)
            w = x
        ans -= B[x] - 2
    else:
        if x < h:
            A[x:h] = [w] * (h - x)
            h = x
        ans -= A[x] - 2

print(ans)
