N = int(input())
ls = input().split(' ')
dic = { i for i in ls }
if len(dic) == N:
    print('YES')
else:
    print('NO')
