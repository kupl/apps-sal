n = int(input())
timeList = list(map(int, input().split()))
m = int(input())
argList = [list(map(int, input().split())) for _ in range(m)]

# 普通にやると
res_time = sum(timeList)

for a in argList:

    # a[0]問目を解くのに　a[1]秒かかるよ
    print((res_time - timeList[a[0] - 1] + a[1]))
