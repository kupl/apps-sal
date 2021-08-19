lst = list(map(int, input().split()))
lst.sort()
if lst[0] == 5 and lst[1] == 5 and (lst[2] == 7):
    print('YES')
else:
    print('NO')
