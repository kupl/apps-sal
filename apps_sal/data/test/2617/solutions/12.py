import math

def __starting_point():
    t = int(input())
    for numtests in range(t):
        n = int(input())
        d = math.floor(math.log(n, 2))
        if n == 2:
            print("1")
            print("0")
        elif n == 3:
            print("1")
            print("1")
        else:
            print(str(d))
            for i in range(d-2):
                print(str(int(2**(i))), end = " ")
            if n < int(3*(2**(d-1))):
                print(str(math.floor((n+1-2**d)/2)), end = " ")
                print(str((n+1)%2))
            else:
                print(str(int(2**(d-2))), end = " ")
                print(str(int(n+1-3*(2**(d-1)))))
__starting_point()
