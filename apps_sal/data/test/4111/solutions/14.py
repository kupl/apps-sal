n = int(input())
a = list(map(int, input().split()))
sum1 = [0]
sum2 = [0]
for i in range(n):
    if i % 2 == 0:
        sum1.append(sum1[-1] + a[i])
        sum2.append(sum2[-1])
    else:
        sum2.append(sum2[-1] + a[i])
        sum1.append(sum1[-1])
ans = 0
for i in range(n):
    if i % 2 == 0:
        SUM1 = sum1[i]
        SUM2 = sum2[i]
        SUM1, SUM2 = SUM1 + sum2[-1] - SUM2, SUM2 + sum1[-1] - a[i] - SUM1
        if SUM1 == SUM2:
            ans += 1
    else:
        SUM1 = sum1[i]
        SUM2 = sum2[i]
        SUM1, SUM2 = SUM1 + sum2[-1] - a[i] - SUM2, SUM2 + sum1[-1] - SUM1
        if SUM1 == SUM2:
            ans += 1       
print(ans)
