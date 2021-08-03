n = int(input())
nums = list(map(int, input().split()))
left = {}

for i in range(n):
    if nums[i] in list(left.keys()):
        left[nums[i]] += 1
    else:
        left[nums[i]] = 1

count = 0
done = set()
for i in nums:
    left[i] -= 1
    if left[i] == 0:
        del left[i]
    if i not in done:
        count += len(list(left.keys()))
        done.add(i)

print(count)
