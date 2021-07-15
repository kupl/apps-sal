n = int(input())
nums = list(map(int, input().split()))
nums.sort()
if nums[-1] >= nums[-2] + nums[-3]:
    print('NO')
else:
    print('YES')
    if n % 2 == 0:
        print(*nums[-1:0:-2], *nums[0:n:2])
    else:
        print(*nums[-1:0:-2], nums[0], *nums[1:n:2])        
