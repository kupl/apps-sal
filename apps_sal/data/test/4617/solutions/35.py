line1 = input()
line2 = input()
my_list1 = []
my_list2 = []

for i in line1:
    my_list1.append(i)

for i in line2:
    my_list2.append(i)

my_list2.reverse()

if my_list1 == my_list2:
    print('YES')
else:
    print('NO')
