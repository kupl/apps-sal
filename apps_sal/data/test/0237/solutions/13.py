n, m, k = list(map(int, input().split()))

min_delta = min(k - 1, n - k)
max_delta = max(k - 1, n - k)

top = ((k - 1) * k + (n - k) * (n - k + 1)) // 2 + (max_delta - min_delta) * min_delta + max_delta + 1


def get_level(n, k, level):
    return 1 + min(level, k - 1) + min(level, n - k)


if top <= m:
    print(max_delta + 1 + (m - top) // n)
else:
    add = m - n
    curr_level = 0
    while add >= get_level(n, k, curr_level):
        add -= get_level(n, k, curr_level)
        curr_level += 1
    print(curr_level + 1)
