from heapq import heappush, heappop

N, M = map(int, input().split())
AtoB = [[] for _ in range(M + 1)]
for i in range(N):
    A, B = map(int, input().split())
    if A > M:
        continue
    AtoB[A].append(B)

# A が小さい順に増えていく
result = 0
que = []  # ヒープ
for Bs in AtoB:
    for B in Bs:
        heappush(que, -B)  # Python3 のヒープはデフォルトで小さい順
    if que:
        result -= heappop(que)
print(result)
