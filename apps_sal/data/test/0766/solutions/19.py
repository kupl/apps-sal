s = list(input())
s.sort()
if len(s) < 4:
    print("No")
else:
    st = set(s)
    if len(st) > 4:
        print("No")
    elif len(st) < 2:
        print("No")
    elif len(st) == 2:
        c1 = s.count(s[0])
        c2 = s.count(s[-1])
        if c1 < 2 or c2 < 2:
            print("No")
        else:
            print("Yes")
    else:
        print("Yes")

