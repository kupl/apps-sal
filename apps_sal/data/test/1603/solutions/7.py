n = int(input())
price = list(map(int, input().split()))
price_s = list(price)
price_s.sort()
m = int(input())
pre_sum = [price[0]]
pre_sum1 = [price_s[0]]

out = []

for i in range(1, n, 1):
    ele = price[i] + pre_sum[i - 1]

    pre_sum.append(ele)
    ele1 = price_s[i] + pre_sum1[i - 1]
    pre_sum1.append(ele1)
# print(pre_sum)
# print(pre_sum1)
for i in range(m):
    full = False
    curr = list(map(int, input().split()))
    ind1 = curr[2] - 1

    ind2 = curr[1] - 2
    if ind2 < 0:
        full = True
    if curr[0] == 1:
        if full:
            out.append(pre_sum[ind1])
        else:

            lis1 = pre_sum[ind1]
            lis2 = pre_sum[ind2]
            out.append(lis1 - lis2)
    else:
        if full:
            out.append(pre_sum1[ind1])
        else:

            lis1 = pre_sum1[ind1]
            lis2 = pre_sum1[ind2]
            out.append(lis1 - lis2)
for i in range(m):
    print(out[i])
