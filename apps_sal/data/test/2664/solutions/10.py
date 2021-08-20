import sys
ans = 1
print(1)
sys.stdout.flush()
print(4, 1, 4, 2, 2)
sys.stdout.flush()
print(2, 3, 4)
sys.stdout.flush()
result = int(input())
if result == 1:
    ans = 3
elif result == 3:
    ans = 1
elif result == 4:
    ans = 2
elif result == 2:
    print(1)
    sys.stdout.flush()
    print(1, 4)
    sys.stdout.flush()
    print(1, 5)
    sys.stdout.flush()
    r1 = int(input())
    if r1 == -1:
        ans = 5
    elif r1 == 1:
        ans = 4
print(2)
sys.stdout.flush()
print(ans)
sys.stdout.flush()
