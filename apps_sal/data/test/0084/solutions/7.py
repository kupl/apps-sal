
n = int(input())

biggest_num = 2 * n - 1

if all([x == '9' for x in str(biggest_num)]):
    lead_digit = 0
    length = len(str(biggest_num))
elif all([x == '9' for x in str(biggest_num)[1:]]):
    lead_digit = int(str(biggest_num)[0])
    length = len(str(biggest_num)) - 1
else:
    lead_digit = int(str(biggest_num)[0]) - 1
    length = len(str(biggest_num)) - 1


result = 0
for i in range(lead_digit + 1):
    desired_num = int(str(i) + '9' * length)
    if desired_num == 0:
        continue
    result += (min([n, desired_num - 1]) - max([desired_num // 2, desired_num - n]))


print(result)
