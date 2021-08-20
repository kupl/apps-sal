import sys
print(1)
print(4, 1, 2, 2, 3)
print(4, 1, 4, 4, 5)
sys.stdout.flush()
a = int(input())
if a == 0:
    print(2)
    print(1)
elif a == 2:
    print(2)
    print(2)
elif a == -2:
    print(2)
    print(4)
elif a == 1:
    print(2)
    print(3)
else:
    print(2)
    print(5)
