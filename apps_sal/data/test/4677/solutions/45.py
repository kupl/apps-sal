first_str = input()
input_list = list(first_str)
total_list = list()
for i in input_list:
    if i == '0':
        total_list.append('0')
    elif i == '1':
        total_list.append('1')
    elif not total_list:
        pass
    else:
        total_list.pop(-1)
total = ''.join([str(_) for _ in total_list])
print(total)
