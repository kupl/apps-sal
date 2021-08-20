nums = list(map(int, input().split()))
if nums.count(5) == 2 and nums.count(7) == 1:
    print('YES')
else:
    print('NO')
