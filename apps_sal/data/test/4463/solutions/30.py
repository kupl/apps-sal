s = str(input())
t = str(input())

# 文字列sをソート（sortedをすると配列型になるのでjoinして上げる必要あり）
sort_s_list = sorted(s)
sort_s = "".join(sort_s_list)

# 文字列tを逆ソート
t_list = list(t)
t_list.sort(reverse=True)
reverse_sort_t = "".join(t_list)

if sort_s < reverse_sort_t:
    print("Yes")
else:
    print("No")
