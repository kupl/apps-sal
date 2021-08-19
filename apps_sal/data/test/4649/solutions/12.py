def solve(d, n, k):
    mv = sum(d[0:k])
    v = mv
    for i in range(1, n - k + 1):
        mv = mv + d[i + k - 1] - d[i - 1]
        v = min(v, mv)
    return v


for _ in range(int(input())):
    (n, k) = tuple(map(int, input().split()))
    s = input()
    st = 'RGB' * (n // 3 + 3)
    (diff1, diff2, diff3) = ([0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)])
    for i in range(n):
        if s[i] != st[i]:
            diff1[i] = 1
        if s[i] != st[i + 1]:
            diff2[i] = 1
        if s[i] != st[i + 2]:
            diff3[i] = 1
    print(min(solve(diff1, n, k), solve(diff2, n, k), solve(diff3, n, k)))
