lst = input().split()
A = int(lst[0])
B = int(lst[1])
if A * B % 2 == 1:
    print('Yes')
else:
    print('No')
