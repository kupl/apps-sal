def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
s = [frozenset(x) for x in input().split()]
s = set(s)
print(len(s))
