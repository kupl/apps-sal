x = int(input())
if x % 4 == 1:
    print(0, 'A')
    return
if x % 4 == 3:
    print(2, 'A')
    return
if x % 4 == 0:
    print(1,'A')
    return
if x % 4 == 2:
    print(1, 'B')
