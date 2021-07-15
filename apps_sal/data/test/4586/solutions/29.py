n = list(input())
list01 = list(set(n[0:3]))
list02 = list(set(n[1:4]))
if len(list01) == 1 or len(list02) == 1:
    print('Yes')
else:
    print('No')
