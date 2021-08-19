def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


(n, m) = mi()
a = li()
b = li()
a = [x % 2 for x in a]
b = [x % 2 for x in b]
ans = min(a.count(0), b.count(1)) + min(a.count(1), b.count(0))
print(ans)
