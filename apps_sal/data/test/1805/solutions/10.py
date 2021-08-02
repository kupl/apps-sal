for i in range(int(input())):
    a = int(input())
    if a <= 4:
        print(4 - a)
    elif a % 2 == 1:
        print(1)
    else:
        print(0)
