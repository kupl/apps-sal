a = map(int, input().split())
input_list = list(a)

group_a = [1, 3, 5, 7, 8, 10, 12]
group_b = [4, 6, 9, 11]
group_c = [2]
list_of_list = [group_a, group_b, group_c]

count_match = 0

for list_i in list_of_list:
    if input_list[0] in list_i and input_list[1] in list_i:
        count_match += 1
        break

if count_match == 1:
    print('Yes')
else:
    print('No')
