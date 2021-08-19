N = int(input())
cnt_list = []
for i in range(1, N + 1):
    cnt = 0
    while i >= 1:
        if i % 2 == 0:
            cnt += 1
            i = i / 2
        else:
            break
    cnt_list.append(cnt)
M = cnt_list.index(max(cnt_list))
print(M + 1)
