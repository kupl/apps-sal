n, z = [int(i) for i in input().split(' ')]
nums = [int(i) for i in input().split(' ')]

nums.sort()
if n % 2 == 0:
    odd = nums[:n//2]
    even = nums[n//2:]
else:
    odd = nums[:n//2]
    even = nums[n//2+1:]

i, j = 0, 0
res = 0
while i < len(odd) and j < len(even):
    if abs(odd[i] - even[j]) >= z:
        res += 1
        i += 1
        j += 1
    else:
        j += 1
print(res)
