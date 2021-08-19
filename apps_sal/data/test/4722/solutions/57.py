lst = input().split()
A = int(lst[0])
B = int(lst[1])
if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0:
    print('Possible')
else:
    print('Impossible')
