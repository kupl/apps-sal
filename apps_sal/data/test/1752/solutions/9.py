def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
a = li()
a.sort(reverse=True)
(x, y) = ([], [])
for i in range(1, n):
    (x if i % 2 else y).append(a[i])
ans = x[::-1] + [a[0]] + y
print(*ans)
