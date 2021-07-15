from math import sin, pi, cos
def solve():
    n = int( input())
    return(cos(pi/(4*n))/sin(pi/(2*n)))
    
def main():
    t = int( input())
    print("\n".join( map( str, [ solve() for _ in range(t)])))
def __starting_point():
    main()

__starting_point()
