h, w = (int(i) for i in input().split())
list_a = [input() for s in range(0, h)]
list_tmp = []
for i in range(0, h):
    for j in range(0, w):
        if list_a[i][j] == '#':
            list_tmp.append(list(list_a[i]))
            break
# 転置... https://note.nkmk.me/python-list-transpose/　参照
list_tmp_t = [list(x) for x in zip(*list_tmp)]
list_tmp2 = []
for i in range(0, len(list_tmp_t)):
    for j in range(0, len(list_tmp_t[i])):
        if list_tmp_t[i][j] == '#':
            list_tmp2.append(list(list_tmp_t[i]))
            break
# 転置... https://note.nkmk.me/python-list-transpose/　参照
list_ans = [list(x) for x in zip(*list_tmp2)]
for i in range(0, len(list_ans)):
    print("".join(list_ans[i]))
