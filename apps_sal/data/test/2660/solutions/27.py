import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

from heapq import heapify,heappop,heappush
def main():
    Q = int(input())
    total_b = 0
    total_a = 0
    less_than_middle = 0
    left = []
    right = []
    cnt = 0
    for _ in range(Q):
        query = tuple(map(int,input().split()))
        if query[0] == 1:
            a,b = query[1:]
            total_b += b
            total_a += a
            cnt += 1
            heappush(right,a)
            while left and right and (-left[0] > right[0]):
                p = -heappop(left)
                q = heappop(right)
                heappush(left,-q)
                heappush(right,p)
                less_than_middle += -p + q
            if cnt%2 == 0:
                p = heappop(right)
                heappush(left,-p)
                less_than_middle += p
        else:
            if cnt%2 == 0:
                x = -left[0]
                ans = total_a - 2*less_than_middle + total_b
                print(x,ans)
            else:
                x = right[0]
                ans = total_a - 2*less_than_middle - x + total_b
                print(x,ans)
def __starting_point():
    main()
__starting_point()
