import sys
import heapq

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def solve():
    n = int(input())
    A = [int(i) for i in input().split()]
    heap = []
    nxt = n

    for i in range(n):
        tmp = []
        heapq.heappush(heap, -A[i])
        while heap and -heap[0] == nxt:
            tmp.append(-heapq.heappop(heap))
            nxt -= 1
        print(*tmp)

def __starting_point():
    solve()
__starting_point()
