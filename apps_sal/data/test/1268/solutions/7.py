def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
a = li()
b = li()
b.sort()
print('YES' if sum(a) <= b[-1] + b[-2] else 'NO')
