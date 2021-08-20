nums = sorted(list(map(int, input().split())), reverse=True)
K = int(input())
print(nums[0] * 2 ** K + nums[1] + nums[2])
