def main():
    n, m = [int(t) for t in input().split()]

    tail_length = [0 for _ in range(n)]

    adj_list = [set() for _ in range(n)]

    for _ in range(m):
        u, v = [int(t) - 1 for t in input().split()]
        adj_list[u].add(v)
        adj_list[v].add(u)

    tail_length[0] = 1
    beauty = tail_length[0] * len(adj_list[0])

    for u in range(1, n):
        candidate_tail_lengths = [tail_length[v] + 1 for v in adj_list[u] if v < u]
        if len(candidate_tail_lengths) != 0:
            tail_length[u] = max(candidate_tail_lengths)
        else:
            tail_length[u] = 1
        beauty = max(beauty, tail_length[u] * len(adj_list[u]))

    print(beauty)


def __starting_point():
    main()


__starting_point()
