import sys
print('1')
sys.stdout.flush()
print('3 1 2 2')
sys.stdout.flush()
print('3 3 4 4')
sys.stdout.flush()
d = int(input())
if d == 2:
    print('2')
    sys.stdout.flush()
    print('2')
    sys.stdout.flush()
elif d == 1:
    print('2')
    sys.stdout.flush()
    print('1')
    sys.stdout.flush()
elif d == -1:
    print('2')
    sys.stdout.flush()
    print('3')
    sys.stdout.flush()
elif d == -2:
    print('2')
    sys.stdout.flush()
    print('4')
    sys.stdout.flush()
else:
    print('2')
    sys.stdout.flush()
    print('5')
    sys.stdout.flush()

