def main():
    from collections import defaultdict, Counter
    n, m, k = list(map(int, input().split()))
    n += 1
    cc = [0, *list(map(int, input().split()))]
    l = list(range(n))
    for _ in range(m):
        a, b = list(map(int, input().split()))
        u, v = a, b
        while u != l[u]:
            u = l[u]
        while v != l[v]:
            v = l[v]
        if u > v:
            l[u] = v
            while a != v:
                a, l[a] = l[a], v
        elif u < v:
            l[v] = u
            while b != u:
                b, l[b] = l[b], u
    groups = defaultdict(Counter)
    for i, g in enumerate(l):
        if i != g:
            l[i] = g = l[g]
            groups[g][cc[i]] += 1
    for g, v in list(groups.items()):
        v[cc[g]] += 1
    print(sum(sum(v.values()) - v.most_common(1)[0][1] for v in list(groups.values())))


def __starting_point():
    main()

__starting_point()
