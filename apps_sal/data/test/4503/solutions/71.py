h, n = map(int, input(). split())
list01 = input().split()
list02 = [int(a) for a in list01]
if sum(list02) >= h:
    print('Yes')
else:
    print('No')
