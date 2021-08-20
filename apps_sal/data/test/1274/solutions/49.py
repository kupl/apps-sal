import heapq
(n, m) = map(int, input().split())
que = []
for _ in range(n):
    (a, b) = map(int, input().split())
    que.append((-b, a))
que.sort(key=lambda x: x[1], reverse=True)


def solve(que, m):
    ans = 0
    h = []
    heapq.heapify(h)
    for i in range(1, m + 1):
        while len(que) != 0 and que[-1][1] <= i:
            tmp = que.pop()
            heapq.heappush(h, tmp)
        if len(h) == 0:
            continue
        tmp = heapq.heappop(h)
        ans -= tmp[0]
    return ans


print(solve(que, m))
