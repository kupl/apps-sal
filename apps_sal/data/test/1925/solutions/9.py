import sys
def input(): return sys.stdin.readline().rstrip()
 
 
def main():
    a,b,n=map(int, input().split())
    if b<=n:
        n=b-1
    print(((a*n)//b) - (a*(n//b)))
    

    
 
def __starting_point():
    main()
__starting_point()
