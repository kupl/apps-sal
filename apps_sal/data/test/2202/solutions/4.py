n, m = [int(x) for x in input().split(' ')]
numbers = [int(x) for x in input().split(' ')]

max_res = 0
total_sum = sum(numbers)
sum_thus_far = 0
for i in range(n - 1):
    tmp_a = sum_thus_far + numbers[i]
    tmp_b = total_sum - tmp_a
    tmp_sum = (tmp_a % m) + (tmp_b % m)
    if tmp_sum > max_res:
        max_res = tmp_sum

print(max_res)
