def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
a = li()
a = [0] + a + [1001]
ans = 0
i = 0
while i <= n:
    j = i + 1
    while j <= n + 1 and a[j] == a[j - 1] + 1:
        j += 1
    ans = max(ans, j - i - 2)
    i = j
print(ans)
