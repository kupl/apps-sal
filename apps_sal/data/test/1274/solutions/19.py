def main():
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline
    from heapq import heappush, heappop

    N, M = list(map(int, input().split()))
    AB = [ [] for _ in range(100000) ]

    for _ in range(N):
        a, b = list(map(int, input().split()))
        AB[a-1].append(-b)

    ans = 0
    heap = []
    for a in range(M):
        for b in AB[a]:
            heappush(heap, b)
        if heap:
            ans -= heappop(heap)
    
    print(ans)

main()

