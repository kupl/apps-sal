def isEven(a, b):
    if a % 2 == 0:
        return True
    if b % 2 == 0:
        return True
    return False


i = input().split()
a = int(i[0])
b = int(i[1])
if isEven(a, b):
    print('Even')
else:
    print('Odd')
