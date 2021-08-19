(a, b) = map(int, input().split())
x = [1, 3, 5, 7, 8, 10, 12]
y = [4, 6, 9, 11]
if a == 2 or b == 2:
    print('No')
elif a in x and b in x:
    print('Yes')
elif a in y and b in y:
    print('Yes')
else:
    print('No')
