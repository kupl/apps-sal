a = list(map(int, input().split()))
sum = 0
for i in range(a[0]):
    if i == 0:
        sum = a[1]
    else:
        sum *= a[1] - 1
print(sum)
