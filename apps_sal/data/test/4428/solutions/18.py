n = int(input())
a = [int(i) for i in input().split()]
i = -1
j = n
sum1 = 0
sum2 = 0
ans = 0
while i < j:
    while (sum1 <= sum2) and (i < j):
        i += 1
        if i == j:
            break
        sum1 += a[i]
        if (sum1 == sum2) and (sum1 > ans):
            ans = sum1
    while (sum2 <= sum1) and (j > i):
        j -= 1
        if i == j:
            break
        sum2 += a[j]
        if (sum1 == sum2) and (sum1 > ans):
            ans = sum1

print(ans)
