import sys
print(1)
print(1, 1)
print(1, 2)
sys.stdout.flush()
a = int(input())
if (a == 1):
    print(2)
    print(1)
    sys.exit()
elif (a == -1):
    print(2)
    print(2)
    sys.exit()
print(1)
print(1, 3)
print(1, 4)
sys.stdout.flush()
b = int(input())
if (b == 1):
    print(2)
    print(3)
elif (b == -1):
    print(2)
    print(4)
else:
    print(2)
    print(5)
