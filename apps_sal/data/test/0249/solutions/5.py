__author__ = "zabidon"

n, l, x, y = map(int, input().split())
data = set(map(int, input().split()))

old_x = any(i + x in data for i in data)
old_y = any(i + y in data for i in data)

if old_x and old_y:
    print(0)
elif old_x:
    print(1)
    print(y)
elif old_y:
    print(1)
    print(x)
else:
    found = False
    for i in data:
        if i + x + y in data:
            found = True
            print(1)
            print(i + x)

        elif i + x - y in data:
            if 0 <= i + x <= l:
                found = True
                print(1)
                print(i + x)

            if not found and 0 <= i - y <= l:
                found = True
                print(1)
                print(i - y)
        if found:
            break

    if not found:
        print(2)
        print(x, y)
