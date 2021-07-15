a = [int(i) for i in input().split()]
ans = "NO"
for i in range(0, 4):
    for j in range(i + 1, 5):
        for k in range(j + 1, 6):
            sum1 = a[i] + a[j] + a[k]
            sum2 = 0
            for x in range(6):
                if x != i and x != j and x != k:
                    sum2 += a[x]
            if sum1 == sum2:
                ans = "YES"
print(ans)
