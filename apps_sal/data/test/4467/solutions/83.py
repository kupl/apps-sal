N = int(input())
r = []
for i in range(N):
    r.append(list(map(int, input().split())))
b = []
for i in range(N):
    b.append(list(map(int, input().split())))
r = sorted(r, key=lambda x: x[0])
b = sorted(b, key=lambda x: x[0])
r_selected = [False] * N
ans = 0
for i in range(N):
    y_max = -1
    j_selected = -1
    for j in range(N):
        if r_selected[j]:
            continue
        if b[i][0] > r[j][0] and b[i][1] > r[j][1]:
            if y_max < r[j][1]:
                y_max = r[j][1]
                j_selected = j
    if y_max == -1:
        continue
    else:
        r_selected[j_selected] = True
print(r_selected.count(True))
