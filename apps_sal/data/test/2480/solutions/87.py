def main():
    from collections import defaultdict, deque

    N, K = list(map(int, input().split()))
    a = list(map(int, input().split()))

    def accumulate(a, mod):
        s = 0
        yield s
        for x in a:
            s = (s + x - 1) % mod
            yield s

    acc = accumulate(a, mod=K)

    d = defaultdict(int)
    dq = deque()
    ans = 0
    for x in acc:
        if x in d:
            ans += d[x]
        d[x] += 1
        dq.append(x)
        if len(dq) >= K:
            r = dq.popleft()
            d[r] -= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
