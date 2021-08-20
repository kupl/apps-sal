def main():
    from collections import Counter
    (n, m, _) = map(int, input().split())
    cc = list(map(int, input().split()))
    (pairs, avail) = ([[] for _ in range(n)], [True] * n)
    for _ in range(m):
        (a, b) = map(int, input().split())
        pairs[a - 1].append(b - 1)
        pairs[b - 1].append(a - 1)
    for (a, f) in enumerate(avail):
        if f:
            (stack, cnt, avail[a]) = ([a], Counter(), False)
            while stack:
                a = stack.pop()
                cnt[cc[a]] += 1
                for b in pairs[a]:
                    if avail[b]:
                        avail[b] = False
                        stack.append(b)
            n -= cnt.most_common(1)[0][1]
    print(n)


def __starting_point():
    main()


__starting_point()
