def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


(n, k) = mi()
ans = (n * 2 + k - 1) // k + (n * 5 + k - 1) // k + (n * 8 + k - 1) // k
print(ans)
