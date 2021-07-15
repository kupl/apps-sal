n = int(input())
a = list(map(int,input().split()))
nums = []
total = 0
for num in a:
    total += num
    nums.append(total)
minVal = 10 ** 9 * 2 + 1
for i in range(n - 1):
    sub = total - nums[i]
    minVal = min(abs(sub - nums[i]), minVal)
print(minVal)
