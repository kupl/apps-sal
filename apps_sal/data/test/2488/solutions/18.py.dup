from heapq import heappop, heappush, heapify
N, D, A = list(map(int, input().split()))
B = []
for _ in range(N):
    x, h = list(map(int, input().split()))
    B.append((x, h))
heapify(B)

dic = {}

ans = 0
atk_cnt = 0
while B:
    x, h = heappop(B)
    if h == -1:
        atk_cnt -= dic[x - 1]
        continue
    if h <= A * atk_cnt:
        continue
    h -= A * atk_cnt
    sup = x + 2 * D
    bomb = (h - 1) // A + 1
    ans += bomb
    dic[sup] = bomb
    atk_cnt += bomb
    heappush(B, (sup + 1, -1))


print(ans)
