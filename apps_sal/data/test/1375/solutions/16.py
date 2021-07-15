3

input()
nums = list(map(int, input().split()))
sum_n = sum(nums)
ans = current_sum = one_third = 0
for x in nums[:-1]:
    current_sum += x
    if current_sum == 2 / 3 * sum_n:
        ans += one_third
    if current_sum == 1 / 3 * sum_n:
        one_third += 1
print(ans)
