t = int(input().strip())
for _ in range(t):
    a,b = list(map(int,input().strip().split()))
    #nums = [int(i) for i in input().strip().split()]
    if a == b:
        print(0)
    elif a > b:
        if (a - b)%2 == 0:
            print(1)
        else:
            print(2)
    else:
        if (b - a)%2 != 0:
            print(1)
        else:
            print(2)

