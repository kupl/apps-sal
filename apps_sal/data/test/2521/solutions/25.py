from heapq import heapify, heappushpop

def abc062_d():
    n = int(input())
    A = list(map(int, input().split()))

    front = A[:n]
    fsum = [0] * (3*n)
    fsum[n-1] = sum(front)
    heapify(front)
    for i in range(n, 2*n):
        fmin = heappushpop(front, A[i])
        fsum[i] = fsum[i-1] + A[i] - fmin

    back = [-1*a for a in A[2*n:]]
    bsum = [0] * (3*n)
    bsum[2*n] = -1 * sum(back)
    heapify(back)
    for i in range(2*n-1, n-1, -1):
        bmax = -1 * heappushpop(back, -1*A[i])
        bsum[i] = bsum[i+1] + A[i] - bmax

    ans = -10**18
    for i in range(n-1, 2*n):
        ans = max(ans, fsum[i] - bsum[i+1])
    print(ans)

def __starting_point():
    abc062_d()
__starting_point()
