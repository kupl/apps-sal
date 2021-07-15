import sys

def H(x,y):
    r = x*x+2*x*y+x+1
    return r

def main():
    input = sys.stdin.readline()
    r = int(input)
    x = 1
    q = r - 3
    while q > 0:
        if q % (2*x) == 0:
            y = q // (2*x)
            print(x,y)
            break
        else:
            x += 1
            q = r - 1 - x - x*x
    if q <= 0:
        print("NO")
#    return output

def __starting_point():
    main()
__starting_point()
