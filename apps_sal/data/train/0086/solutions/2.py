#OM GANESHAY NAMH
#GANPATI BAPPA MORYA
import math,queue,heapq 
import sys 
sys.setrecursionlimit(10**6)
fastinput=sys.stdin.readline
fastout=sys.stdout.write
t=int(fastinput()) 
while t:
    t-=1
    n=int(fastinput()) 
    a=list(map(int,fastinput().split()))  
    c=a.count(1) 
    if c==0 or c==n:
        print(n)
        print(*a) 
    elif c<=n//2:
        print(n-c)
        print('0 '*(n-c)) 
    else:
        if c%2==0:
            print(c)
            print('1 '*c) 
        else:
            c-=1 
            print(c) 
            print('1 '*c)
