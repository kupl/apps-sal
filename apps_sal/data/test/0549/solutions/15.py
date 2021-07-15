import math

def displaysize(n):
    s = int(math.floor(math.sqrt(n)))  
    while n % s != 0:
        s -= 1
    return (s,n//s)

def __starting_point():
    i = int(input())
    a,b = displaysize(i)
    print(str(a) + "   " + str(b))


__starting_point()
