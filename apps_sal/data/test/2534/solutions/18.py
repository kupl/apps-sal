(n, m) = map(int, input().split())
min_lst = []
max_lst = [[]] * m
mx = [0] * m
for r in range(n):
    tmp = list(map(int, input().split()))
    mn = tmp[0]
    tmp_lst = []
    j = 0
    for i in tmp:
        if i > mx[j]:
            mx[j] = i
            max_lst[j] = [(r, j, i)]
        elif i == mx[j]:
            max_lst[j].append((r, j, i))
        if i < mn:
            mn = i
            tmp_lst = [(r, j, i)]
        elif i == mn:
            tmp_lst.append((r, j, i))
        j += 1
    min_lst.extend(tmp_lst)
flg = False
for i in max_lst:
    for j in i:
        if j in min_lst:
            print(j[2])
            flg = True
            exit(0)
if not flg:
    print('GUESS')
