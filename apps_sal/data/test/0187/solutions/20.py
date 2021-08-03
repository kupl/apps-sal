from collections import defaultdict

n = int(input())
arr = []
nums = set()
f = defaultdict(int)

for _ in range(n):
    arr.append(int(input()))

if n % 2 == 1:
    print("NO")
    return

for num in arr:
    nums.add(num)
    f[num] += 1
    if len(nums) > 2:
        print("NO")
        return

nums = list(nums)

if len(nums) == 2:
    if f[nums[0]] == f[nums[1]]:
        print("YES")
        print(nums[0], nums[1])
        return

print("NO")
