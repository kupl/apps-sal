n = int(input())
data = list(map(int, input().split()))
nums = set(data)
if len(nums) <= 2:
    print('YES')
elif len(nums) == 3:
    tmp = list(sorted(list(nums)))
    if tmp[1] - tmp[0] == tmp[2] - tmp[1]:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
