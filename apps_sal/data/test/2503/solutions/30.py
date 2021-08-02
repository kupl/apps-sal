import numpy as np

n, k = list(map(int, input().split()))
xyc = [list(input().split()) for _ in range(n)]

b = np.zeros((3 * k - 1, 2 * k - 1), np.int64)

for x, y, c in xyc:
    x = int(x)
    y = int(y)

    q, r = divmod(x, k)
    if q % 2:
        y += k
    x = r

    if c == "W":
        y += k

    y %= 2 * k

    b[y][x] += 1

b[:k, k:] = b[k:2 * k, :k - 1]
b[k:2 * k, k:] = b[:k, :k - 1]
b[2 * k:, :] = b[:k - 1, :]

b = np.pad(b, (1, 0), "constant")

b = np.cumsum(b, axis=0)
b = np.cumsum(b, axis=1)

cnt = b[k:, k:] - b[k:, :-k] - b[:-k, k:] + b[:-k, :-k]
ans = cnt.max()
print(ans)
