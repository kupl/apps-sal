import heapq

def solve():
    N = int(input())
    que = []
    for i in range(N):
        a, b = list(map(int, input().split()))
        heapq.heappush(que, (b, a))
    now = 0
    while que:
        b, a = heapq.heappop(que)
        now += a
        if now > b:
            return False
    return True

if solve():
    print("Yes")
else:
    print("No")

