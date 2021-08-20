q = int(input())
for wrere in range(q):
    (a, b) = map(int, input().split())
    if a < b:
        if (a - b) % 2 == 1:
            print(1)
        else:
            print(2)
    elif a == b:
        print(0)
    elif (a - b) % 2 == 0:
        print(1)
    else:
        print(2)
