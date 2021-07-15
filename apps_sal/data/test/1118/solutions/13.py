n = int(input())
raw_list = [int(item) for item in input().split()]

l = [raw_list[0]]
for item in raw_list[1:]:
    if item != l[-1]:
        l.append(item)
n = len(l)

dp1 = []
dp2 = [0] * (n + 1)
for i in range(2, n + 1):
    dp = []
    for j in range(n - i + 1):
        if l[j] == l[i + j - 1]:
            dp.append(min(dp1[j + 1], dp2[j], dp2[j + 1]) + 1)
        else:
            dp.append(min(dp2[j], dp2[j + 1]) + 1)
    dp1, dp2 = dp2, dp
res = dp2[0]
print(res)

