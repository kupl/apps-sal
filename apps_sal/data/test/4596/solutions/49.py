N = int(input())
A_lst = list(map(int, input().split()))
cnt = 0
A_lst_c = []
for i in range(N):
    while A_lst[i] % 2 == 0:
        A_lst[i] //= 2
        cnt += 1
    if i == 0:
        pass
    else:
        cnt = cnt - A_lst_c[i-1]
    A_lst_c.append(cnt)
A_lst_c_min = min(A_lst_c)
print(A_lst_c_min)
