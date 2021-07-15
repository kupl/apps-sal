N = int(input())
A_ls = list(input().split(' '))
A_set = { i for i in A_ls }
if len(A_set) == N:
    print('YES')
else:
    print('NO')
