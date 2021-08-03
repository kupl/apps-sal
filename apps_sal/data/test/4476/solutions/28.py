t = int(input())

for i in range(t):
    line = input()
    [a, b] = [int(x) for x in line.split(' ')]

    if a == b:
        print(0)

    if a > b:
        if a % 2 == b % 2:
            print(1)
        else:
            print(2)

    elif a < b:
        if a % 2 == b % 2:
            print(2)
        else:
            print(1)
