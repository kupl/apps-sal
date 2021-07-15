def __starting_point():

    n = int( input() )
    locs = [int(x) for x in input().split()]

    for i in range(n):

        if i == 0:
            minres = locs[i+1] - locs[i]
            maxres = locs[-1] - locs[i]
        elif i == n-1:
            minres = locs[i] - locs[i-1]
            maxres = locs[i] - locs[0]
        else:
            minres = min( locs[i] - locs[i-1] , locs[i+1] - locs[i] )
            maxres = max( locs[i] - locs[0] , locs[-1] - locs[i] )

        print( minres , maxres )
        

__starting_point()
