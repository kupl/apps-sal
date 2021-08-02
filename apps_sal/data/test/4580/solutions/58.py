n = int(input())
l = list(map(int, input().split()))

ans = [0 for i in range(8)]
rate_3200 = 0

for i in l:
    if 1 <= i <= 399:
        ans[0] += 1
    elif 400 <= i <= 799:
        ans[1] += 1
    elif 800 <= i <= 1199:
        ans[2] += 1
    elif 1200 <= i <= 1599:
        ans[3] += 1
    elif 1600 <= i <= 1999:
        ans[4] += 1
    elif 2000 <= i <= 2399:
        ans[5] += 1
    elif 2400 <= i <= 2799:
        ans[6] += 1
    elif 2800 <= i <= 3199:
        ans[7] += 1
    elif 3200 <= i:
        rate_3200 += 1

if rate_3200 == 0:
    num = 8 - ans.count(0)
    print(("{} {}".format(num, num)))
else:
    count_0 = ans.count(0)
    if count_0 == 8:
        min_num = 1
        max_num = rate_3200
    else:
        min_num = 8 - count_0
        max_num = 8 - count_0 + rate_3200
    print(("{} {}".format(min_num, max_num)))
