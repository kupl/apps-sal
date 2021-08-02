
def main():
    import heapq
    import sys
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    CD = [tuple(map(int, input().split())) for _ in range(Q)]

    maximum = 2 * 10**5

    B = [[] for _ in range(maximum)]
    member = [set() for _ in range(maximum)]
    belongs = [-1] * N

    for i, (a, b) in enumerate(AB):
        b -= 1
        heapq.heappush(B[b], (-a, i))
        member[b].add(i)
        belongs[i] = b

    maximum_list = []
    for i, b in enumerate(B):
        if len(b) > 0:
            heapq.heappush(maximum_list, (-b[0][0], i))

    Inf = [0] * maximum
    for c, d in CD:
        c -= 1
        d -= 1
        before = belongs[c]
        belongs[c] = d
        member[before].remove(c)
        member[d].add(c)
        for i in Inf:
            if len(B[before]) <= 0:
                break
            if B[before][0][1] in member[before]:
                break
            else:
                heapq.heappop(B[before])

        if len(B[before]) > 0:
            heapq.heappush(maximum_list, (-B[before][0][0], before))

        heapq.heappush(B[d], (-AB[c][0], c))
        heapq.heappush(maximum_list, (AB[c][0], d))
        for i in Inf:
            minmum, num = maximum_list[0]
            if len(B[num]) == 0 or -B[num][0][0] != minmum:
                heapq.heappop(maximum_list)
            else:
                print(minmum)
                break


main()
