def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n = ii()
a = li()
a.sort()
(i, j) = (0, n - 1)
ans = 0
while i < j:
    ans += (a[i] + a[j]) ** 2
    i += 1
    j -= 1
print(ans)
