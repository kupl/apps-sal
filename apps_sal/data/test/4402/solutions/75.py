a, b = map(int,input().split())

if a >= 13:
    print(b)
elif a >= 6 and a <= 12:
    print(int(b / 2))
else:
    print(0)
