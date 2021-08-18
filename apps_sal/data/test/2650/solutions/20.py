def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, q = map(int, input().split())
    from collections import defaultdict
    from heapq import heappush, heappop
    h = defaultdict(lambda: [])
    saikyo = []
    A, B = [], []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        heappush(h[b], (-a, i))
    for i in h:
        x = h[i][0]
        heappush(saikyo, (-x[0], x[1]))
    for i in range(q):
        c, d = map(int, input().split())
        c -= 1
        cfrom = B[c]
        B[c] = d
        while h[cfrom]:
            x = h[cfrom][0]
            if B[x[1]] != cfrom:
                heappop(h[cfrom])
                continue
            heappush(saikyo, (-x[0], x[1]))
            break
        heappush(h[d], (-A[c], c))
        while h[d]:
            x = h[d][0]
            if B[x[1]] != d:
                heappop(h[d])
                continue
            heappush(saikyo, (-x[0], x[1]))
            break

        while saikyo:
            x = saikyo[0]

            y = h[B[x[1]]][0]
            if -y[0] != x[0]:
                heappop(saikyo)
                continue
            print(x[0])
            break

    print()


def __starting_point():
    main()


__starting_point()
