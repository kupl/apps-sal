from heapq import heappop, heappush
N = int(input())
R = []
B = []
YFlag = [True] * (2 * N)
for _ in range(N):
    (a, b) = map(int, input().split())
    R.append((a, b))
for _ in range(N):
    (c, d) = map(int, input().split())
    B.append((c, d))
B.sort()
ans = 0
for (c, d) in B:
    cand = []
    for (a, b) in R:
        if a < c and b < d and YFlag[b]:
            cand.append(b)
    if cand:
        ans += 1
        YFlag[max(cand)] = False
print(ans)
