n = int(input())
a = list(map(int, input().split()))
s = max(a)
sx = a.index(s)
t = min(a)
tx = a.index(t)
if t >= 0:
    print(n - 1)
    for i in range(n - 1):
        print(str(i + 1) + ' ' + str(i + 2))
elif s <= 0:
    print(n - 1)
    for i in reversed(range(n - 1)):
        print(str(i + 2) + ' ' + str(i + 1))
else:
    print(2 * n - 1)
    if abs(s) >= abs(t):
        for i in range(n):
            print(str(sx + 1) + ' ' + str(i + 1))
        for i in range(n - 1):
            print(str(i + 1) + ' ' + str(i + 2))
    elif abs(s) < abs(t):
        for i in range(n):
            print(str(tx + 1) + ' ' + str(i + 1))
        for i in reversed(range(n - 1)):
            print(str(i + 2) + ' ' + str(i + 1))
