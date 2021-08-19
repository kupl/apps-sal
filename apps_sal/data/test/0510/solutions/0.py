def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


(a, b, c, d) = mi()
(a, b, c) = sorted([a, b, c])
ans = max(0, d - (b - a)) + max(0, d - (c - b))
print(ans)
