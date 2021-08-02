L, R = map(int, input().split())
k = 0
l = 2020
m = 2020
apList = [0] * 2019
for i in range(L, R + 1):
    k = i % 2019
    if apList[k] != 0:
        break
    else:
        apList[k] += 1
res = 2018
for i in range(2019):
    for j in range(i + 1, 2019):
        if apList[i] != 0 and apList[j] != 0:
            res = min(i * j % 2019, res)
print(res)
