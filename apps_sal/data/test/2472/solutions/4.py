import heapq


def solve():
    N = int(input())
    que = []
    for i in range(N):
        a, b = list(map(int, input().split()))
        heapq.heappush(que, (-b, a))
    now = 10 ** 10
    while que:
        b, a = heapq.heappop(que)
        b = -b
        if now > b:
            now = b
        now -= a
        if now < 0:
            return False
    return True


if solve():
    print("Yes")
else:
    print("No")
