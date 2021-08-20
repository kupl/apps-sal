def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
a = [li() for _ in range(n)]
k = ii()
ans = 0
for (l, r) in a:
    ans += k <= r
print(ans)
