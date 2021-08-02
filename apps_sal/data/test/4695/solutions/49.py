a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
x, y = map(int, input().split())
if (x in a and y in a) or (x in b and y in b): print('Yes')
else: print('No')
