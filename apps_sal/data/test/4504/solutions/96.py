s = input()
for i in range(1, 101):
    s_del_end = s[:len(s) - i]
    len_s_del_end = len(s_del_end)
    if s_del_end[:len_s_del_end // 2] == s_del_end[len_s_del_end // 2:] and len_s_del_end % 2 == 0:
        print(len_s_del_end)
        return
