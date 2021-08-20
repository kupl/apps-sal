n = int(input().strip())
nums = list(map(int, input().strip().split()))
if all([num % 2 for num in nums]) or all([not num % 2 for num in nums]):
    print(' '.join(map(str, nums)))
else:
    nums.sort()
    print(' '.join(map(str, nums)))
