def split1(m, n, k):
    if k < m:
        return m // (k + 1) * n
    else:
        return n // (k - m + 2)


def split(m, n, k):
    r = max(split1(m, n, k), split1(n, m, k))
    return r if r else -1


args = input().split()
print(split(*list(map(int, args))))
