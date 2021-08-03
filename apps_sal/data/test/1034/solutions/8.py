def main():
    import heapq

    x, y, z, k, *abc = list(map(int, open(0).read().split()))
    a = sorted(abc[:x], reverse=True)
    b = sorted(abc[x:x + y], reverse=True)
    c = sorted(abc[x + y:], reverse=True)
    s = set()

    h = [(-(a[0] + b[0] + c[0]), 0, 0, 0)]
    heapq.heapify(h)
    num = []
    for _ in range(k):
        p, i, j, k = heapq.heappop(h)
        num.append(-p)
        for p, q, r in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            p, q, r = min(i + p, x - 1), min(j + q, y - 1), min(k + r, z - 1)
            if (p, q, r) not in s:
                s.add((p, q, r))
                v = - (a[p] + b[q] + c[r])
                heapq.heappush(h, (v, p, q, r))

    ans = '\n'.join(map(str, num))
    print(ans)


def __starting_point():
    main()


__starting_point()
