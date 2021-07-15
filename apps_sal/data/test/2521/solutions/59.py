import heapq
def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = []
    heapq.heapify(q)
    frnt = [None]*3*n
    back = [None]*3*n
    heapq.heappush(q, a[0])
    frnt[0] = a[0]
    for i in range(1, 2*n+1):
        frnt[i] = a[i]
        frnt[i] += frnt[i-1]
        heapq.heappush(q, a[i])
        if n <= i:
            frnt[i] -= heapq.heappop(q)
    q = []
    heapq.heapify(q)
    heapq.heappush(q, -1*a[3*n-1])
    back[3*n-1] = a[3*n-1]
    for i in reversed(range(n-1, 3*n-1)):
        back[i] = a[i]
        back[i] += back[i+1]
        heapq.heappush(q, -1*a[i])
        if i < 2*n:
            back[i] += heapq.heappop(q)
    ans = -float("inf")
    for i in range(n-1, 2*n):
        ans = max(ans, frnt[i] - back[i+1])
    print(ans)

def __starting_point():
    main()
__starting_point()
