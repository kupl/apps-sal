def f_f():
    import numpy as np

    n = int(input())
    x, y = np.array([input().split() for _ in range(n)], dtype="int64").T

    a = np.arctan2(x, y)
    i = a.argsort()
    x, y, a = x[i], y[i], a[i]

    x, y = np.concatenate([x, x]), np.concatenate([y, y])
    a = np.concatenate([a, a + 2 * np.pi])

    xcs, ycs = x.cumsum(), y.cumsum()
    items = np.arange(1, n + 1)[None, :]
    l = np.arange(n)[:, None]

    dx = xcs[l + items - 1] - xcs[l] + x[l]
    dy = ycs[l + items - 1] - ycs[l] + y[l]

    print(((dx * dx + dy * dy).max()**0.5))


def __starting_point():
    f_f()


__starting_point()
