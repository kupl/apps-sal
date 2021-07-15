import sys

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    L = pow(2, N)
    Inf = pow(10, 20)
    Dist = [Inf] * L
    
    Dist[0] = 0
    for _ in range(M):
        a, b = map(int, input().split())
        bit = 0
        C = [int(c) for c in input().split()]
        for c in C: bit += pow(2, c-1)
        for k, d in enumerate(Dist):
            if d < Inf: Dist[k | bit] = min(Dist[k | bit], d + a)
            
    print(Dist[L - 1] if Dist[L-1] < Inf else -1)

    return 0

def __starting_point():
    solve()
__starting_point()
