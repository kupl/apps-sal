import heapq
N, K = list(map(int, input().split()))

L = [[] for _ in range(N)]
All = []
s = set([])
for i in range(N):
    t, d = list(map(int, input().split()))
    t -= 1  # 0スタートに
    heapq.heappush(L[t], -d)  # 最大から取り出したいので負にする。
    heapq.heappush(All, [-d, t])  # すべてから大きい順に取り出せるように
    s.add(t)

# print(L,s)
point = 0
ns = 0  # 現在の種類
later = []
now = []
syurui = set([])
while len(now) < K and All:
    temp = heapq.heappop(All)
    if temp[1] not in syurui:
        ns += 1
        point -= temp[0]
        syurui.add(temp[1])
        heapq.heappush(now, -1 * temp[0])
    else:
        later.append(temp)
for i in later:
    heapq.heappush(All, i)

point += ns * ns
while len(now) < K:
    temp = heapq.heappop(All)
    point -= temp[0]
    heapq.heappush(now, -1 * temp[0])

# print(ns,point)
# print(now,All,All[0][0])
while All and now[0] < -1 * All[0][0]:
    temp = heapq.heappop(All)
    dele = heapq.heappop(now)
    # print(temp,dele)
    upoint = point - temp[0] - dele - ns * ns + (ns - 1)**2
    # print(upoint,point)
    if upoint >= point:
        point = upoint
        ns -= 1
    else:
        break

print(point)
# print(All)
# print(now)
