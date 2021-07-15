import sys
def I():
        return sys.stdin.readline().rstrip()

for _ in range(int(I())):
    n = int(I())
    a = list( map( int, I().split() ) )
    d = dict()
    for i, x in enumerate(a):
        if x in d:
            n = min( n, i - d[ x ] )
        d[ x ] = i
    print( n + 1 if n < len(a) else -1 )

