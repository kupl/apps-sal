
n = int(input())
nums = list(map(int, input().split()))

i = 0
longest = 1
while i < n - 1:
    length = 1
    while i+1 < n and nums[i]*2 >= nums[i+1]:
        i += 1
        length += 1
    longest = max(longest, length)
    i += 1

print(longest)



