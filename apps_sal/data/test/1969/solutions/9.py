def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
a = [input().strip() for i in range(n)]
ans = sum((a[i][j] == a[i - 1][j - 1] == a[i - 1][j + 1] == a[i + 1][j - 1] == a[i + 1][j + 1] == 'X' for i in range(1, n - 1) for j in range(1, n - 1)))
print(ans)
