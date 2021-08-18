def main():
    import sys
    def input(): return sys.stdin.readline().rstrip("\r\n")
    mod = 10**9 + 7

    ans = []

    n, q = map(int, input().split())
    y = [[] for _ in range(2 * 10**5)]
    data = [(0, 0)] * n
    import heapq
    for i in range(n):
        a, b = map(int, input().split())
        data[i] = (a, b - 1)
        heapq.heappush(y[b - 1], (-a, i))
    max_rate = []
    max_rate_list = [()] * (2 * 10**5)
    for i in range(2 * 10**5):
        if y[i]:
            s, t = heapq.heappop(y[i])
            heapq.heappush(max_rate, (-s, t, i))
            heapq.heappush(y[i], (s, t))
            max_rate_list[i] = (-s, t)
    from collections import defaultdict
    ng_num = defaultdict(set)
    for _ in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        a, b = data[c]
        data[c] = (a, d)
        heapq.heappush(y[d], (-a, c))
        ng_num[b].add(c)
        if c in ng_num[d]:
            ng_num[d].discard(c)
        while y[b]:
            s, t = heapq.heappop(y[b])
            if t not in ng_num[b]:
                heapq.heappush(max_rate, (-s, t, b))
                heapq.heappush(y[b], (s, t))
                max_rate_list[b] = (-s, t)
                break
        while y[d]:
            s, t = heapq.heappop(y[d])
            if t not in ng_num[d]:
                heapq.heappush(max_rate, (-s, t, d))
                heapq.heappush(y[d], (s, t))
                max_rate_list[d] = (-s, t)
                break
        while max_rate:
            s, t, r = heapq.heappop(max_rate)
            if t not in ng_num[r] and (s, t) == max_rate_list[r]:
                ans.append(s)
                heapq.heappush(max_rate, (s, t, r))
                break
    print(*ans, sep="\n")


main()
