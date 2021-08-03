h, w, m = list(map(int, input().split()))
a_list = []
b_list = []
h_list = [0 for _ in range(h)]
w_list = [0 for _ in range(w)]
for i in range(m):
    a, b = list(map(int, input().split()))
    a_list.append([a, b])
    h_list[a - 1] += 1
    w_list[b - 1] += 1
h_max = max(h_list)
w_max = max(w_list)
w_flag = [0 for _ in range(w)]
for i in range(w):
    if w_list[i] == w_max:
        w_flag[i] = 1
h_flag = [0 for _ in range(h)]
for i in range(h):
    if h_list[i] == h_max:
        h_flag[i] = 1
flag = 0
for i in range(m):
    if h_flag[a_list[i][0] - 1] == 1 and w_flag[a_list[i][1] - 1] == 1:
        flag += 1
s = sum(h_flag) * sum(w_flag)
print((h_max + w_max - 1 if flag == s else h_max + w_max))
