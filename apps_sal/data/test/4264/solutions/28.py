n = int(input())
s = len(str(n))
if s == 1:
    print(n)
elif s == 2:
    print(9)
elif s == 3:
    print(n - 90)
elif s == 4:
    print(9 + 900)
elif s == 5:
    print(9 + 900 + n - 10000 + 1)
else:
    print(90909)
