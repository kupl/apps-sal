(a, b) = map(int, input().split())
x = [1, 3, 5, 7, 8, 10, 12]
y = [4, 6, 9, 11]
if a in x and b in x or (a in y and b in y):
    print('Yes')
else:
    print('No')
