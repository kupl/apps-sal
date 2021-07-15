N = int(input())
A_ls = input().split(' ')
rst = set()
for i in A_ls:
    rst.add(i)
if len(rst) == N:
    print('YES')
else:
    print('NO')
