import heapq

N = int(input())
ns = [int(x) for x in input().strip().split(' ')]

largest = N
storage = []

for n in ns:
    if n != largest:
        heapq.heappush(storage, -n)
        print()
    else:
        print(n, end=' ')
        largest -= 1
        while len(storage) > 0 and storage[0] == -largest:
            print(-heapq.heappop(storage), end=' ')
            largest -= 1

        print()
