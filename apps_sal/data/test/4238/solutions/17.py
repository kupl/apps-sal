n_l = list(str(input()))
sum_num = 0
for i in n_l:
    sum_num += int(i)
if sum_num % 9 == 0 or sum_num == 0:
    print('Yes')
else:
    print('No')
