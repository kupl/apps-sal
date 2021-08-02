n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    if nums[0] == 1:
        print("YES")
    else:
        print("NO")
else:
    if nums.count(1) == n - 1:
        print("YES")
    else:
        print("NO")
