(n, m, x) = list(map(int, input().split()))
inp = []
for i in range(n):
    tmp = list(map(int, input().split()))
    inp.append(tmp)
sum = 0
min = 10 ** 10
for i in range(2 ** n):
    tmp = [0] * m
    flg = 0
    for j in range(n):
        if i >> j & 1:
            sum += inp[j][0]
            for k in range(1, m + 1):
                tmp[k - 1] += inp[j][k]
    for (ii, k) in enumerate(tmp):
        if k < x:
            flg = 1
            break
    if sum < min and flg == 0:
        min = sum
    sum = 0
if min == 10 ** 10:
    min = -1
print(min)
