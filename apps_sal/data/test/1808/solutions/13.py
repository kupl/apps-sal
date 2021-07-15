n, k, x = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

partial_sum = 0
for i in range(n - k):
    partial_sum += nums[i]

print(partial_sum + k * x)

