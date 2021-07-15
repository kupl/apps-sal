N = int(input())
A_ls = list(input().split(' '))
rst = { i for i in A_ls }
if len(rst) == N:
    print('YES')
else:
    print('NO')
