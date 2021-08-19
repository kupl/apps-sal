import sys
import heapq
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def main():
    (N, Q) = [int(x) for x in input().split()]
    hsize = 2 * 10 ** 5 + 1
    h = [[] for _ in range(hsize)]
    C = [0] * N
    A = []
    for i in range(N):
        (a, b) = [int(x) for x in input().split()]
        A.append(a)
        heapq.heappush(h[b], (-a, i))
        C[i] = b
    A = tuple(A)
    byodo = []
    for i in range(1, hsize):
        if len(h[i]) == 0:
            continue
        x = h[i][0]
        heapq.heappush(byodo, (-x[0], x[1]))
    ans = []
    for _ in range(Q):
        (c, d) = [int(x) for x in input().split()]
        c -= 1
        cfrom = C[c]
        C[c] = d
        while h[cfrom]:
            x = h[cfrom][0]
            if C[x[1]] != cfrom:
                heapq.heappop(h[cfrom])
                continue
            heapq.heappush(byodo, (-x[0], x[1]))
            break
        heapq.heappush(h[d], (-A[c], c))
        while h[d]:
            x = h[d][0]
            if C[x[1]] != d:
                heapq.heappop(h[d])
                continue
            heapq.heappush(byodo, (-x[0], x[1]))
            break
        while byodo:
            x = byodo[0]
            y = h[C[x[1]]][0]
            if -y[0] != x[0]:
                heapq.heappop(byodo)
                continue
            ans.append(x[0])
            break
    print('\n'.join(map(str, ans)))


def __starting_point():
    main()


__starting_point()
