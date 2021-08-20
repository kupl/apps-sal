(N, K) = map(int, input().split())
List = list(map(int, input().split()))
INF = 10000000000
expList = [INF] * 1001


def expectationF(num):
    if expList[num] == INF:
        exp = 0
        for i in range(1, num + 1):
            exp += i / num
        expList[num] = exp
    return expList[num]


res = 0
mid = 0
midList = []
for i in range(N):
    if i >= 1:
        midList.append(expectationF(List[i]) + midList[i - 1])
    else:
        midList.append(expectationF(List[i]))
m = K - 1
for j in range(N - m):
    if j == 0:
        mid = midList[j + m]
    else:
        mid = midList[j + m] - midList[j - 1]
    res = max(res, mid)
print(res)
