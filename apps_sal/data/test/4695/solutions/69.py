(x, y) = map(int, input().split())
A = [1, 3, 5, 7, 8, 10, 12]
B = [4, 6, 9, 11]
C = [2]
if x in A and y in A:
    check = True
elif x in B and y in B:
    check = True
elif x in C and y in C:
    check = True
else:
    check = False
print('Yes' if check else 'No')
