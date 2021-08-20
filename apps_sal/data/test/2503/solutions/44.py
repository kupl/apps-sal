import numpy as np
(n, k) = list(map(int, input().split()))


def get_bound(x):
    if x < k - 1:
        return [(0, x + 1), (x + k + 1, 2 * k)]
    else:
        return [(x - k + 1, x + 1)]


blacks = [[0] * (2 * k + 1) for _ in range(2 * k + 1)]
for _ in range(n):
    (x, y, c) = input().split()
    x = int(x) % (2 * k)
    y = int(y) % (2 * k) if c == 'B' else (int(y) + k) % (2 * k)
    for shift in [0, k]:
        for (b, t) in get_bound((y + shift) % (2 * k)):
            for (l, r) in get_bound((x + shift) % (2 * k)):
                blacks[b][l] += 1
                blacks[t][l] -= 1
                blacks[b][r] -= 1
                blacks[t][r] += 1
ans = np.max(np.cumsum(np.cumsum(blacks, axis=1), axis=0))
print(int(ans))
