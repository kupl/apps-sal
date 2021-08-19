a = map(int, input().split())
input_set = set(a)
group_a = {1, 3, 5, 7, 8, 10, 12}
group_b = {4, 6, 9, 11}
group_c = {2}
list_of_list = [group_a, group_b, group_c]
count_match = 0
for set_i in list_of_list:
    if set_i.issuperset(input_set):
        count_match += 1
        print('Yes')
        break
if not count_match >= 1:
    print('No')
