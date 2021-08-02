n = int(input())

ans = 0
flag = 0
for i in range(n, 1000):
    s = str(i)
    n_list = list(s)
    if n_list[0] == n_list[1] and n_list[1] == n_list[2] and flag == 0:
        flag = 1
        ans = i

print(ans)
