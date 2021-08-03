n = int(input())
a_list = input().split()
if len(a_list) == len(set(a_list)):
    print('YES')
else:
    print('NO')
