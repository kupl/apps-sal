(n, k) = list(map(int, input().split()))
arr = [int(x) for x in input().split(' ')]
num = 10000000000
for i in range(0, k):
    sum = 0
    for j in range(0, int(n / k)):
        sum += arr[j * k + i]
    if sum < num:
        num = sum
        ans = i + 1
print(str(ans))
