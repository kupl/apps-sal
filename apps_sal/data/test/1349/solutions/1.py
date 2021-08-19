t = int(input())
for _ in range(t):
    (n, k) = [int(v) for v in input().split()]
    x = [int(v) - 1 for v in input().split()]
    ans = 0
    covered = [False] * n
    while not all(covered):
        for xi in x:
            for pos in range(max(0, xi - ans), min(n - 1, xi + ans) + 1):
                covered[pos] = True
        ans += 1
    print(ans)
