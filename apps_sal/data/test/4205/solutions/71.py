n = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)

not_equal = 0
for p, q in zip(nums, sorted_nums):
    if p != q:
        not_equal += 1

if not_equal <= 2:
    print('YES')
else:
    print('NO')
