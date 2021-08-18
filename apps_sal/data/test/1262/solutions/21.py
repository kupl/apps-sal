import math

n = int(input())
cityNo = [0] * n
for i in range(n):
    cityNo[i] = list(map(int, input().split()))
cost = list(map(int, input().split()))
ks = list(map(int, input().split()))

powerStation = [0] * n

totalCost = 0

req_Powerstation = []
notReq_Powerstation = []
totalCost = 0
established = {}
updated = [-1] * n

for j in range(n):

    city = -1
    mini = 9999999999999999
    for i in range(n):
        if mini > cost[i] and i not in established:
            city = i
            mini = cost[i]
    if updated[city] == -1:
        req_Powerstation.append(city + 1)
    else:
        notReq_Powerstation.append([city + 1, updated[city] + 1])
    totalCost += cost[city]
    established[city] = 1

    for i in range(n):

        cost_From_City = (ks[i] + ks[city]) * (abs(cityNo[i][0] - cityNo[city][0]) + abs(cityNo[i][1] - cityNo[city][1]))

        if cost_From_City < cost[i]:
            cost[i] = cost_From_City
            updated[i] = city

print(totalCost)
print(len(req_Powerstation))
print(*req_Powerstation)
print(len(notReq_Powerstation))
for i in range(len(notReq_Powerstation)):
    print(*notReq_Powerstation[i])
