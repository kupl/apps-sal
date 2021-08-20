(n, a) = input().split()
n = int(n)
a = int(a)
if a % 2 == 1:
    print(int(a / 2 + 1))
else:
    print(int(n / 2 - a / 2 + 1))
