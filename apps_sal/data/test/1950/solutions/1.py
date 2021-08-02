import heapq


def solve(heap, n):
    heapq.heapify(heap)
    ans = 0
    while(n > 1):
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        z = heapq.heappop(heap)
        heapq.heappush(heap, x + y + z)
        ans += x + y + z
        n -= 2

    return ans


n = int(input())
a = list(map(int, input().split()))
a.sort()

if n % 2 == 0:
    delta = a[0] + a[1]
    a = [delta] + a[2:]
    n -= 1
    print(solve(a, n) + delta)
else:
    print(solve(a, n))
