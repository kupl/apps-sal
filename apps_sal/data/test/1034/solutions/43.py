def main():
    import heapq
    (x, y, z, k, *abc) = list(map(int, open(0).read().split()))
    a = sorted(abc[:x], reverse=True)
    b = sorted(abc[x:x + y], reverse=True)
    c = sorted(abc[x + y:], reverse=True)
    s = set()
    h = [(-(a[0] + b[0] + c[0]), 0, 0, 0)]
    heapq.heapify(h)
    num = []
    for _ in range(k):
        (p, i, j, k) = heapq.heappop(h)
        num.append(-p)
        for (p, q, r) in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            if i + p < x and j + q < y and (k + r < z):
                if (i + p, j + q, k + r) not in s:
                    s.add((i + p, j + q, k + r))
                    v = -(a[i + p] + b[j + q] + c[k + r])
                    heapq.heappush(h, (v, i + p, j + q, k + r))
    ans = '\n'.join(map(str, num))
    print(ans)


def __starting_point():
    main()


__starting_point()
