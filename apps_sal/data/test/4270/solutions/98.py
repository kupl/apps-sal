import heapq

def main():
    n = int(input())
    values = [int(i) for i in input().split()]
    heapq.heapify(values)
    for i in range(n-1):
        a = heapq.heappop(values)
        b = heapq.heappop(values)
        heapq.heappush(values, (a+b)/2)
    ans = heapq.heappop(values)
    print(ans)

def __starting_point():
    main()
__starting_point()
