import heapq
(n, s) = map(int, input().split())
applications_sell = []
applications_buy = []
for i in range(n):
    (cur1, cur2, cur3) = map(str, input().split())
    if cur1 == 'S':
        heapq.heappush(applications_sell, [cur1, int(cur2), int(cur3)])
    else:
        heapq.heappush(applications_buy, [cur1, -int(cur2), int(cur3)])
glass_sell = []
if len(applications_sell):
    glass_sell.append(heapq.heappop(applications_sell))
while len(applications_sell) > 0:
    cur = heapq.heappop(applications_sell)
    if glass_sell[-1][1] == cur[1]:
        glass_sell[-1][2] += cur[2]
    else:
        glass_sell.append(cur)
glass_buy = []
if len(applications_buy):
    glass_buy.append(heapq.heappop(applications_buy))
while len(applications_buy) > 0:
    cur = heapq.heappop(applications_buy)
    if glass_buy[-1][1] == cur[1]:
        glass_buy[-1][2] += cur[2]
    else:
        glass_buy.append(cur)
for i in range(min(len(glass_sell), s) - 1, -1, -1):
    print(glass_sell[i][0], glass_sell[i][1], glass_sell[i][2])
for i in range(min(len(glass_buy), s)):
    print(glass_buy[i][0], -glass_buy[i][1], glass_buy[i][2])
