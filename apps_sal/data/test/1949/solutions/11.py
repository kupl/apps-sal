(n, k) = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()
subbed = 0
i = 0
while k > 0:
    valid = i < n
    if not valid:
        print(0)
        k -= 1
        continue
    num = nums[i]
    i += 1
    if num == subbed:
        continue
    tosub = num - subbed
    print(tosub)
    k -= 1
    subbed = num
