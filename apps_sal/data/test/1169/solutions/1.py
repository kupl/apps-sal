def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


(n, m) = mi()
x = max(0, n - 2 * m)
for i in range(n + 1):
    c = i * (i - 1) // 2
    if c >= m:
        y = n - i
        break
print(x, y)
