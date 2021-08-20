(N, M) = map(int, input().split())
H = list(map(int, input().split()))
ways = [list(map(int, input().split())) for i in range(M)]
observatoryList = [1] * N
for i in range(M):
    if H[ways[i][0] - 1] <= H[ways[i][1] - 1]:
        observatoryList[ways[i][0] - 1] = 0
    if H[ways[i][0] - 1] >= H[ways[i][1] - 1]:
        observatoryList[ways[i][1] - 1] = 0
goodObservatoryCount = observatoryList.count(1)
print(goodObservatoryCount)
