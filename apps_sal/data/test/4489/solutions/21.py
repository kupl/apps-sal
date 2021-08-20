N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]
s_dic = {}
t_dic = {}
for i in s:
    if i in s_dic.keys():
        s_dic[i] += 1
    else:
        s_dic[i] = 1
for i in t:
    if i in t_dic.keys():
        t_dic[i] += 1
    else:
        t_dic[i] = 1
all_list = []
for i in s_dic.keys():
    if i in t_dic.keys():
        all_list.append(s_dic[i] - t_dic[i])
    else:
        all_list.append(s_dic[i])
for i in t_dic.keys():
    if i in s_dic.keys():
        all_list.append(s_dic[i] - t_dic[i])
    else:
        all_list.append(-t_dic[i])
print(max(max(all_list), 0))
