lst = input().split()
if len(lst) == len(set(lst)):
    print('3')
if len(lst) - 1 == len(set(lst)):
    print('2')
if len(lst) - 2 == len(set(lst)):
    print('1')
