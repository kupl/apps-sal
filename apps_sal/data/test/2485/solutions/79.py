import sys
h, w, m = list(map(int, input().split()))
h_lst = [[0, i] for i in range(h)]
w_lst = [[0, i] for i in range(w)]
memo = []

for i in range(m):
    x, y = list(map(int, input().split()))
    h_lst[x - 1][0] += 1
    w_lst[y - 1][0] += 1
    memo.append((x - 1, y - 1))

h_lst.sort(reverse=True)
w_lst.sort(reverse=True)
Max_h = h_lst[0][0]
Max_w = w_lst[0][0]
h_ans = [h_lst[0][1]]
w_ans = [w_lst[0][1]]
if h != 1:
    s = 1
    while s < h and h_lst[s][0] == Max_h:
        h_ans.append(h_lst[s][1])
        s += 1
if w != 1:
    t = 1
    while t < w and w_lst[t][0] == Max_w:
        w_ans.append(w_lst[t][1])
        t += 1


memo = set(memo)

# 探索するリストは、最大を取るものの集合でなければ計算量はO(m)にはならない！
for j in h_ans:
    for k in w_ans:
        if (j, k) not in memo:
            print((Max_h + Max_w))
            return
print(((Max_h + Max_w) - 1))
