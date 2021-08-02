def cnt_sum(str_num):
    sum = 0
    for a in str_num:
        sum += ord(a) - ord('0')
    return sum


str_a = input().strip()
max_sum = cnt_sum(str_a)
ans = str_a
cnt_digit = len(str_a)

for i in range(cnt_digit - 1, -1, -1):
    if str_a[i] != '0':
        new_str = str_a[:i] + chr(ord(str_a[i]) - 1) + '9' * (cnt_digit - i - 1)
        cur_sum = cnt_sum(new_str)
        if cur_sum > max_sum:
            max_sum = cur_sum
            ans = new_str

print(int(ans))
