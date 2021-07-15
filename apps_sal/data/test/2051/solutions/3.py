def main():
    from collections import defaultdict, Counter
    n, m, k = list(map(int, input().split()))
    n += 1
    cc = [0, *list(map(int, input().split()))]
    l = list(range(n))

    def find(x):
        while x != l[x]:
            x = l[x]
        return x

    for _ in range(m):
        a, b = list(map(int, input().split()))
        u, v = find(a), find(b)
        if u > v:
            l[u] = v
            while a != v:
                a, l[a] = l[a], v
        elif u < v:
            l[v] = u
            while b != u:
                b, l[b] = l[b], u
    groups = defaultdict(list)
    for i, c in enumerate(cc):
        l[i] = i = find(i)
        groups[i].append(c)
    for v in list(groups.values()):
        n -= Counter(v).most_common(1)[0][1] if len(l) > 1 else 1
    print(n)


def __starting_point():
    main()

__starting_point()
