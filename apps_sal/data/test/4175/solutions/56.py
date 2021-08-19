N = int(input())
alter_str = input()
str_list = [alter_str]
for _ in range(N - 1):
    input_str = input()
    if input_str in str_list:
        print('No')
        break
    if input_str[0] != alter_str[-1]:
        print('No')
        break
    else:
        str_list.append(input_str)
        alter_str = input_str
else:
    print('Yes')
