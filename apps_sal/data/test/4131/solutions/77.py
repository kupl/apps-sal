n, m = list(map(int, input().split()))
p_y = []
for i in range(m):
    p, y = list(map(int, input().split()))
    p_y.append([p, y, i])

p_y_sorted = sorted(p_y)
li_id = []
prev_p = -1
cnt = 1

for i in p_y_sorted:
    if(prev_p != i[0]):
        prev_p = i[0]
        cnt = 1
    id = str(i[0]).zfill(6) + str(cnt).zfill(6)
    li_id.append([i[2], id])
    cnt += 1

li_id_sorted = sorted(li_id)

for i in li_id_sorted:
    print((i[1]))
