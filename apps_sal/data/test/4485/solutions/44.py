import sys
input = sys.stdin.readline


def read():
    N, M = list(map(int, input().strip().split()))
    AB = []
    for i in range(M):
        a, b = list(map(int, input().strip().split()))
        AB.append((a, b))
    return N, M, AB


def solve(N, M, AB):
    is_ok = True
    mid_b = set()
    mid_a = set()
    for a, b in AB:
        if a == 1:
            mid_b.add(b)
        elif b == N:
            mid_a.add(a)
    is_ok = len(mid_a.intersection(mid_b)) > 0
    return "POSSIBLE" if is_ok else "IMPOSSIBLE"


def __starting_point():
    inputs = read()
    print((solve(*inputs)))

__starting_point()
