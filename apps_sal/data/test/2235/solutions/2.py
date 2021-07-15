import bisect

def getIndex(a, x):
    
    for i in range(0, len(a)):
        if  a[i] > x:
            return i
    return 0


n = int(input())

times = []
total = 0
for i in range(0, n):
    time = int(input())
    times.append(time)
    total += time 
    
cost = [0 for i in range(0, n + 1)]
cost[0] = 0
cost[1] = 20

for i in range(2, n + 1):
    cost[i] =  min(cost[i - 1] + 20, 
        cost[bisect.bisect_left(times, times[i-1] - 89)] + 50, 
        cost[bisect.bisect_left(times, times[i-1] - 1439)] + 120)
    
    # print(cost[getIndex(89, times, i - 1)] + 50)
# print(cost)
# print(times)
for i in range(1, n + 1):
    print(cost[i] - cost[i - 1])

