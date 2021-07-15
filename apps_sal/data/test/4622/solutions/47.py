N = int(input())
A_ls = map(int, input().split(' '))
rst = set()
for i in A_ls:
    rst.add(i)
if len(rst) == N:
    print('YES')
else:
    print('NO')
