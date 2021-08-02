N = int(input())
list1 = list(map(int, input().split()))
list1.sort()
max = list1[-1]
min = list1[0]
cost = []
for i in range(min, max + 1):
    tairyoku = 0
    for k in range(N):
        tairyoku += (list1[k] - i)**2
    cost.append(tairyoku)
cost.sort()
print(cost[0])
