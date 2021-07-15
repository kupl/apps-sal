def __starting_point():

    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()

    if a[0] == 1:
        print(-1)
    else:
        print(1)
        

__starting_point()
