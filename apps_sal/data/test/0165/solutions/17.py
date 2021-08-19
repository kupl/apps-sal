def do():
    (b, d, s) = list(map(int, input().split()))
    if b == d == s:
        return 0
    elif b == d and b > s:
        return b - s - 1
    elif b == d and b < s:
        return 2 * (s - b - 1)
    elif b == s and b > d:
        return b - d - 1
    elif b == s and b < d:
        return 2 * (d - b - 1)
    elif d == s and d > b:
        return d - b - 1
    elif d == s and d < b:
        return 2 * (b - d - 1)
    elif b > d and b > s:
        if d > s:
            return 2 * (b - 1 - d) + d - s
        else:
            return 2 * (b - 1 - s) + s - d
    elif d > b and d > s:
        if b > s:
            return 2 * (d - 1 - b) + b - s
        else:
            return 2 * (d - 1 - s) + s - b
    elif b > d:
        return 2 * (s - 1 - b) + b - d
    else:
        return 2 * (s - 1 - d) + d - b


rs = do()
print(rs)
