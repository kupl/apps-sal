def main():
    (N, Q) = [int(n) for n in input().split(' ')]
    edges = [[] for i in range(N)]
    counter = [0] * N
    for i in range(N - 1):
        (a, b) = [int(x) for x in input().split(' ')]
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    for j in range(Q):
        (p, x) = [int(q) for q in input().split(' ')]
        counter[p - 1] += x
    to_visit = [0]
    checked = [1] + [0] * (N - 1)
    tree = [0] * N
    while len(to_visit) > 0:
        visiting = to_visit.pop()
        tree[visiting] += counter[visiting]
        for e in edges[visiting]:
            if checked[e] == 0:
                checked[e] = 1
                to_visit.append(e)
                tree[e] = tree[visiting]
    print(' '.join([str(s) for s in tree]))


main()
