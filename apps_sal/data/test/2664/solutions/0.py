import sys

print(1)
print("3 1 1 2")
print("3 3 3 4")
sys.stdout.flush()

d = int(input())
if d == 0:
    print(2)
    print(5)
    sys.stdout.flush()

elif d == 2:
    print(2)
    print(1)
    sys.stdout.flush()

elif d == 1:
    print(2)
    print(2)
    sys.stdout.flush()

elif d == -2:
    print(2)
    print(3)
    sys.stdout.flush()
else:
    print(2)
    print(4)
    sys.stdout.flush()
