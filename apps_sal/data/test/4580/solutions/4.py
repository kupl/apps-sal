N = int(input())
List = list(map(int, input().split()))
sumList = [0] * 8
mid = 0
for i in range(N):
    if 1 <= List[i] <= 399:
        sumList[0] += 1
    elif 400 <= List[i] <= 799:
        sumList[1] += 1
    elif 800 <= List[i] <= 1199:
        sumList[2] += 1
    elif 1200 <= List[i] <= 1599:
        sumList[3] += 1
    elif 1600 <= List[i] <= 1999:
        sumList[4] += 1
    elif 2000 <= List[i] <= 2399:
        sumList[5] += 1
    elif 2400 <= List[i] <= 2799:
        sumList[6] += 1
    elif 2800 <= List[i] <= 3199:
        sumList[7] += 1
    elif 3200 <= List[i]:
        mid += 1
res1 = 8 - sumList.count(0)
res2 = res1 + mid
if res1 == 0 and mid > 0:
    res1 = 1
print(res1, res2)
