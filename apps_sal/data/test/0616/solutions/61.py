import sys

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Dist = [10 ** 20] * pow(2, N)
    Dist[0] = 0
    for _ in range(M):
        a, b = map(int, input().split())
        C = [int(c) for c in input().split()]
        binaryC = 0
        for c in C: binaryC += pow(2, c-1)
        for j, d in enumerate(Dist):
            if d < 10 ** 20: Dist[j | binaryC] = min(Dist[j | binaryC], Dist[j] + a)
    print(Dist[-1] if Dist[-1] < 10 ** 20 else -1)

    return 0

def __starting_point():
    solve()
__starting_point()
