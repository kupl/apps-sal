n = int(input())
arr = list(map(int, input().split()))
sum1 = 0
sum2 = sum(arr)
min_ = 1 << 60

for i in range(n - 1):
    sum1 += arr[i]
    sum2 -= arr[i]
    min_ = min(min_, abs(sum1 - sum2))
print(min_)
