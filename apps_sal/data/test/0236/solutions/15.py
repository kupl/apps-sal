s = input()

x = s.count('o')
y = len(s) - x

if (x <= 1):
    print("YES")
else:
    if (y % x == 0):
        print("YES")
    else:
        print("NO")
