import sys
x = 1
y = 2
print(x)
print('3 1 1 2')
print('3 3 3 4')
sys.stdout.flush()
weight = eval(input())
if weight == 0:
    print(y)
    print('5')
    sys.stdout.flush()
elif weight == 2:
    print(y)
    print('1')
    sys.stdout.flush()
elif weight == 1:
    print(y)
    print('2')
    sys.stdout.flush()
elif weight == -1:
    print(y)
    print('4')
    sys.stdout.flush()
elif weight == -2:
    print(y)
    print('3')
    sys.stdout.flush()
