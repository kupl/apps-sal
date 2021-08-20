n = int(input())
a = list(map(int, input().split()))
s = sum(a)
nums = {}
for i in range(n):
    if a[i] in nums:
        nums[a[i]] += 1
    else:
        nums[a[i]] = 1
for i in range(int(input())):
    (b, c) = map(int, input().split())
    if b in nums:
        s -= nums[b] * b
        s += nums[b] * c
        if c in nums:
            nums[c] += nums[b]
        else:
            nums[c] = nums[b]
        nums[b] = 0
    print(s)
