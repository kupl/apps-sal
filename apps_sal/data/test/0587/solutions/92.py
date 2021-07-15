import sys
from heapq import heapify, heappop, heappush

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    S = [None] * N
    for i in range(N):
        t, d = map(int, input().split())
        S[i] = (-d, t)
    heapify(S)

    base_point = 0
    appeared_type = set()
    type_Num = 0
    duplicated = []
    heapify(duplicated)
    for i in range(K):
        d, t = heappop(S)
        if t in appeared_type:
            base_point -= d
            heappush(duplicated, -d)
        else:
            base_point -= d
            appeared_type |= {t}
            type_Num += 1

    Ans = base_point + type_Num * type_Num
    while S:
        d, t = heappop(S)
        if t in appeared_type: continue
        else:
            if not duplicated: continue
            else:
                remove = heappop(duplicated)
                base_point -= d + remove
                type_Num += 1
                appeared_type |= {t}
                Ans = max(Ans, base_point + type_Num * type_Num)
    print(Ans)

    return 0

def __starting_point():
    solve()
__starting_point()
