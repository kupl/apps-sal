from heapq import heapify,heappush,heappop

def main():
    N,M = list(map(int,input().split()))
    A = [-x for x in map(int,input().split())]
    heapify(A)
    for i in range(M):
        tmp = -heappop(A)
        tmp2 = tmp//2
        heappush(A,-tmp2)
    ans = 0
    for i in range(N):
        ans += A[i]

    ans = abs(ans)
    return ans

print((main()))

