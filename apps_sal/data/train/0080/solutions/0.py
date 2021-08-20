def solve(L, R):
    res = 0
    for i in range(32):
        for j in range(32):
            l = L >> i << i
            r = R >> j << j
            if l >> i & 1 == 0 or r >> j & 1 == 0:
                continue
            l -= 1 << i
            r -= 1 << j
            if l & r:
                continue
            lr = l ^ r
            ma = max(i, j)
            mi = min(i, j)
            mask = (1 << ma) - 1
            p = bin(lr & mask).count('1')
            ip = ma - mi - p
            res += 3 ** mi * 2 ** ip
    return res


T = int(input())
for _ in range(T):
    (l, r) = list(map(int, input().split()))
    print(solve(r + 1, r + 1) + solve(l, l) - solve(l, r + 1) * 2)
