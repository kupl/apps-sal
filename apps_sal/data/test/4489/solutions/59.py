N = int(input())
n_list = []
for i in range(N):
    n_list.append(input())
M = int(input())
m_list = []
for i in range(M):
    m_list.append(input())
add_dic = {}
for n in n_list:
    add = add_dic.get(n, 0)
    add_dic[n] = add + 1
diff_dic = {}
for m in m_list:
    diff = diff_dic.get(m, 0)
    diff_dic[m] = diff + 1

max_ = 0
for key, add in add_dic.items():
    total = add - diff_dic.get(key, 0)
    if total > max_:
        max_ = total

print(max_)
