def inputIntegerArray():
    return list( map( int, input().split(" ") ) )

def time( t, pos, speed ):
    maxleft = 0
    minright = 1000000000
    for i in range(0,len(pos)):
        distance = speed[i]*t
        left = pos[i]-distance
        right = pos[i]+distance
        maxleft = max( maxleft, left )
        minright = min( minright, right )
    if ( maxleft <= minright ):
        return True
    else:
        return False


(n) = inputIntegerArray()

pos = inputIntegerArray()
speed = inputIntegerArray()

left = 0.0
right = 1000000000.0
for i in range(0,64):
    m = left + ( right - left )/2;
    if ( time( m, pos, speed ) ):
        right = m
    else:
        left = m

print ( left )

