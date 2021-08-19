def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


(n, m, k) = mi()
print('Yes' if min(m, k) >= n else 'No')
