n = int(input())
x = list(map(int, input().split()))
nums = sorted(x)
m1 = n // 2 - 1
m2 = n // 2
for i in range(n):
    if x[i] <= nums[m1]:
        print(nums[m2])
    elif nums[m2] <= x[i]:
        print(nums[m1])
