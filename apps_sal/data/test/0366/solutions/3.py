m, a = map(int, input().split())
if (a % m == 0):
    print(a // m)
else:
    print(a // m + 1)
