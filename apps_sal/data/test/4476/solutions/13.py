t = int(input())
for _ in range(t):
    a, b = [int(x) for x in input().split()]
    if(a == b):
        print(0)
    elif(a > b):
        if((a - b) % 2 == 0):
            print(1)
        else:
            print(2)
    else:
        if((b - a) % 2 == 0):
            print(2)
        else:
            print(1)
