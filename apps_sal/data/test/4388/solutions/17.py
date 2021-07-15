s_l = [n for n in input()]
new_list = []
for i in s_l:
    if i == '9':
        new_list.append(1)
    else:
        new_list.append(9)

print(''.join(map(str, new_list)))
