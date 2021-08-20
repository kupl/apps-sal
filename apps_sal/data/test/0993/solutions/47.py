def main():
    from collections import defaultdict
    import sys
    input = sys.stdin.readline
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    summed = [0 for _ in range(n + 1)]
    d = defaultdict(int)
    for i in range(n):
        summed[i + 1] = (summed[i] + a[i]) % m
    ans = 0
    for j in range(n + 1):
        ans += d[summed[j]]
        d[summed[j]] += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
