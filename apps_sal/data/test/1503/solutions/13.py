def main():
    n, m = [int(c) for c in input().split()]
    if m == 1:
        print(n * (n + 1) // 2)
        return

    testimonies = [[int(c) for c in input().split()] for _ in range(m)]
    perm_map = {client: i for i, client in enumerate(testimonies[0])}
    testimonies = [[perm_map[client] for client in testimonies[i]] for i in range(m)]

    counters = []
    for t in testimonies:
        seq_map = [0] * n
        start, i = 0, 1
        seq_map[t[start]] = 1
        while i < len(t):
            if t[i] - t[i - 1] == 1:
                seq_map[t[start]] += 1
            else:
                cnt = seq_map[t[start]]
                for j in range(start + 1, i):
                    cnt -= 1
                    seq_map[t[j]] = cnt

                start = i
                seq_map[t[start]] = 1
            i += 1

        cnt = seq_map[t[start]]
        for j in range(start + 1, i):
            cnt -= 1
            seq_map[t[j]] = cnt

        counters.append(seq_map)

    ans = sum([min([cnt[i] for cnt in counters]) for i in range(n)])
    print(ans)


def __starting_point():
    main()


__starting_point()
