n, m = map(int, input().split())
a_lst = [str(input()) for _ in range(n)]
b_lst = [str(input()) for _ in range(m)]

flag = False
for i in range(n - m + 1):
    for j in range(n - m + 1):

        count = 0
        if a_lst[i][j] == b_lst[0][0]:
            for k in range(m):
                for l in range(m):
                    if a_lst[i + k][j + l] == b_lst[k][l]:
                        count += 1

            if count == m ** 2:
                flag = True

if flag:
    print('Yes')
else:
    print('No')
