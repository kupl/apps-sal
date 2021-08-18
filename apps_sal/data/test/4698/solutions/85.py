n = int(input())
timeList = list(map(int, input().split()))
m = int(input())
argList = [list(map(int, input().split())) for _ in range(m)]

res_time = sum(timeList)

for a in argList:

    print((res_time - timeList[a[0] - 1] + a[1]))
