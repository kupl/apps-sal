x, y = input().split()
x = int(x)
y = float(y)
if x % 5 == 0 and y - x >= 0.5:
    bal = y - x - 0.5

else:
    bal = y

print('%.2f' % bal)
