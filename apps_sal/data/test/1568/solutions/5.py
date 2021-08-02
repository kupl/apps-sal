n, originCost, decCost, remainCost, T = list(map(int, input().split()))
msgTime = [*list(map(int, input().split()))]
result = 0
for i in range(len(msgTime)):
    nextCost = (T - msgTime[i]) * remainCost + (originCost - decCost * (T - msgTime[i]))
    result += max(nextCost, originCost)
print(result)
