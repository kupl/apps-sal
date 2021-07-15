def main():
    import heapq
    from collections import defaultdict

    x, y, z, k, *abc = map(int, open(0).read().split())
    a = abc[:x]
    b = abc[x:x + y]
    c = abc[x + y:]
    d = defaultdict(list)

    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    h = [(-(a[0] + b[0] + c[0]), 0, 0, 0)]
    heapq.heapify(h)
    ans = []
    for _ in range(k):
        p, i, j, k = heapq.heappop(h)
        ans.append(-p)
        for p, q, r in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            if i + p < x and j + q < y and k + r < z:
                if (j + q, k + r) not in d[i + p]:
                    d[i + p].append((j + q, k + r))
                    v = - (a[i + p] + b[j + q] + c[k + r])
                    heapq.heappush(h, (v, i + p, j + q, k + r))

    print(*ans, sep='\n')


def __starting_point():
    main()

__starting_point()
