import heapq

def __starting_point():

    n,m = map(int,input().split())
    A = list(map(lambda x:int(x)*(-1),input().split()))
    heapq.heapify(A)

    for _ in range(m):
        a = heapq.heappop(A) * (-1)
        a = (a // 2) * (-1)
        heapq.heappush(A,a)

    print(sum(A)*(-1))
__starting_point()
