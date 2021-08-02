def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
ans = 0
for i in range(2, n):
    for j in range(2 * i, n + 1, i):
        ans += j // i
print(ans * 4)
