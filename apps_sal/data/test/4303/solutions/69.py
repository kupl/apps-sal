N,K = list(map(int,input().split()))
x = list(map(int,input().split()))
minTime = 10000000000
for i in range(N-K+1):
    time = 0
    minValue = x[i]
    maxValue = x[i+K-1]
    if minValue < 0 and maxValue < 0:
        time = minValue * -1
    elif minValue >= 0 and maxValue >= 0:
        time = maxValue
    elif minValue < 0 and maxValue >= 0:
        leftTime = minValue * -1
        rightTime = maxValue
        if leftTime < rightTime:
            time = leftTime * 2 + rightTime
        else:
            time = leftTime + rightTime * 2
    if time < minTime:
        minTime = time
print(minTime)
