

n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

kp1_2 = format(k + 1, 'b')
digit_len = len(kp1_2)
sum_nums = sum(nums)

bit_count_dict = {}
for digit in range(digit_len):
    bit_count = 0
    for num in nums:
        if (2 ** digit) & num:
            bit_count += 1
    bit_count_dict[digit] = bit_count

ans = 0
for digit in range(digit_len):
    temp = kp1_2
    ans_candi = sum_nums
    if kp1_2[digit_len - 1 - digit] == '1':
        for d_upper in range(digit + 1, digit_len):
            if kp1_2[digit_len - 1 - d_upper] == '1':
                ans_candi += (n - 2 * bit_count_dict[d_upper]) * 2 ** d_upper
        for d_lower in range(0, digit):
            if n - 2 * bit_count_dict[d_lower] > 0:
                ans_candi += (n - 2 * bit_count_dict[d_lower]) * 2 ** d_lower

        ans = max(ans, ans_candi)

print(ans)
