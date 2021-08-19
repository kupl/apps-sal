list_x = []
for i in range(5):
    list_x.append(int(input()))
max_dif = 0
max_dif_index = 0
for i in range(5):
    if 10 - list_x[i] % 10 > max_dif and list_x[i] % 10 != 0:
        max_dif = 10 - list_x[i] % 10
        max_dif_index = i
ans = list_x.pop(max_dif_index)
tmp = 0
for i in range(4):
    tmp += list_x.pop()
    while tmp % 10 != 0:
        tmp += 1
ans += tmp
print(ans)
