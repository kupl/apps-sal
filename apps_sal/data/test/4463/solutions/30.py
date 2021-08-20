s = str(input())
t = str(input())
sort_s_list = sorted(s)
sort_s = ''.join(sort_s_list)
t_list = list(t)
t_list.sort(reverse=True)
reverse_sort_t = ''.join(t_list)
if sort_s < reverse_sort_t:
    print('Yes')
else:
    print('No')
