def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n = ii()
a = li()
a.sort()
ans = sum((a[i + 1] - a[i] for i in range(0, n, 2)))
print(ans)
