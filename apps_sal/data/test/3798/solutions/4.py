import math


def dsum(b,n):
    if n<b:
        return n
    else:
        return n%b+dsum(b,n//b)

def main():
    n=int(input())
    s=int(input())
    if n == s:
        return n+1
    elif s > (n+1)//2:
        return -1
    else:
        rn = math.floor(math.sqrt(n))
        for i in range(2,rn+1):
            if dsum(i,n) == s:
                return i
        for i in range(rn,0,-1):
            if (n-s) % i == 0:
                b = (n-s)//i+1
                if dsum(b,n) == s:
                    return b
        return -1



print(main())
