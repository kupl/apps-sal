n = int(input())
nums = list(map(int, input().split()))
lastSeen = {}
i = 0
while i < len(nums):
    if nums[i] in lastSeen:
        nums[lastSeen[nums[i]]] = 0
        del lastSeen[nums[i]]
        nums[i] <<= 1
        i -= 1
    else:
        lastSeen[nums[i]] = i
    i += 1
newnums = []
for n in nums:
    if n != 0:
        newnums.append(n)
print(len(newnums))
print(' '.join(map(str, newnums)))
