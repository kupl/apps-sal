# A - Good Integer
#  標準入力N

N = input()
my_list = []
j = 0

for i in N:
    my_list.append(i)

if my_list[0] == my_list[1] == my_list[2] or my_list[1] == my_list[2] == my_list[3]:
    print('Yes')
else:
    print('No')
