a = int(input())
b = int(input())
c = input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
else:
    d = a / b
    print('%.6f' % d)
