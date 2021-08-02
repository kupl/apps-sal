n = int(input())
p = list(map(int, input().split()))

Y = 0
i = 0

while i < n - 2:
    nums = p[i:i + 3]
    if sorted(nums)[-2] == nums[1]:
        Y += 1
    i += 1
print(Y)
