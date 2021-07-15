def __starting_point():
    x1, y1 = [int(x) for x in input().split()]
    x2, y2 = [int(x) for x in input().split()]

    print( max( abs(x1-x2),abs(y1-y2) ) )
__starting_point()
