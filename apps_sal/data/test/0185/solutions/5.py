def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


(n, k) = mi()
if k - 1 > n - k:
    k = n - k + 1
ans = n + k - 1 + 1 + n + n - 1
print(ans)
