n = int(input())
arr = list(map(int, input().split()))
absArr = list(map(abs, arr))
positiveCount, negativeCount = 0, 0
for num in arr:
    if num > 0:
        positiveCount += 1
    elif num < 0:
        negativeCount += 1
if n == 1:
    print(arr[0])
elif positiveCount == n or negativeCount == n:
    print(sum(absArr) - 2 * min(absArr))
else:
    print(sum(absArr))
