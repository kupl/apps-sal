def brute(n, m):
    ans = 0
    for i in range(1, n + 1, 1):
        for j in range(1, n + 1, 1):
            val = (i * i + j * j) % m
            if val == 0:
                ans += 1
    return ans


def solve(n, m):
    cnt = [0] * m
    for i in range(1, m * m + 1, 1):
        upto = n // (m * m)
        extra = n - upto * (m * m)
        if extra >= i:
            upto += 1
        cnt[(i * i) % m] += upto

    ans = 0
    for i in range(0, m):
        for j in range(0, m):
            if (i + j) % m == 0:
                ans += cnt[i] * cnt[j]
    return ans


(n, m) = list(map(int, input().split(' ')))
print(solve(n, m))
