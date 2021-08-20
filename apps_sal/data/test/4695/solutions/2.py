(x, y) = map(int, input().split())
A = [2]
B = [4, 6, 9, 11]
C = [1, 3, 5, 7, 8, 10, 12]
if x in B and y in B:
    print('Yes')
elif x in C and y in C:
    print('Yes')
else:
    print('No')
