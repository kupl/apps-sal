import sys
input = sys.stdin.readline

from fractions import gcd


def main():
    a=int(input())
    b=[]
    for i in range(1,a+1):
        if(gcd(i,a-i)==1 and i<a-i):
            b.append([i/(a-i),[i,a-i]])
    
    b.sort()
    print(b[-1][1][0],b[-1][1][1])
    
main()
