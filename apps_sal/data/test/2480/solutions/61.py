from collections import defaultdict


def main():
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    acca = [0]
    for _a in a:
        acca.append(acca[-1] + _a)
    ans = 0
    cnt = defaultdict(lambda: 0)
    for (i, ac) in enumerate(acca):
        ans += cnt[(ac - i) % k]
        cnt[(ac - i) % k] += 1
        if i >= k - 1:
            cnt[(acca[i - k + 1] - (i - k + 1)) % k] -= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
