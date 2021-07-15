n = int(input())
list01 = input().split()
list02 = sorted([int(s) for s in list01])
a = sum(list02) - list02[-1]
if list02[-1] < a:
    print('Yes')
else:
    print('No')
