import sys
ans = 1
print(1)
sys.stdout.flush()
print(3, 1, 2, 2)
sys.stdout.flush()
print(3, 3, 4, 4)
sys.stdout.flush()
result = int(input())
if result == 1:
    ans = 1
elif result == 2:
    ans = 2
elif result == 0:
    ans = 5
elif result == -1:
    ans = 3
elif result == -2:
    ans = 4
print(2)
sys.stdout.flush()
print(ans)
sys.stdout.flush()
