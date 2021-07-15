N = input()

data_list = str(N)

if data_list[0] == data_list[1] == data_list[2]:
    print('Yes')
elif data_list[1] == data_list[2] == data_list[3]:
    print('Yes')
elif data_list[0] == data_list[1] == data_list[2] == data_list[3]:
    print('Yes')
else:
    print('No')


