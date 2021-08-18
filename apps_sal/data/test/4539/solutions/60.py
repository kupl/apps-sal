n = int(input())
flag = 0
n_str = str(n)
n_len = len(n_str)
n_digit = 0
for i in range(n_len):
    n_digit += int(n_str[i])

if n % n_digit == 0:
    flag = 1


if flag:
    print('Yes')
else:
    print('No')
