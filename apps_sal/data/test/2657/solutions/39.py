import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():


    n = I()
    a = LI()

    mx = max(a)
    a.remove(mx)

    r = (float("inf"), -1)
    half = mx//2
    
    if mx%2 == 0:
        for x in a:
            sa = abs(x-half)
            if sa < r[0]:
                r = (sa, x)
    else:
        for x in a:
            sa = min(abs(x-half), abs(x-(half+1)))
            if sa < r[0]:
                r = (sa, x)

    ans = (mx, r[1])
    print((*ans))
            

                    


main()

