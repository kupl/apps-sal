from sys import stdin,stdout
#from collections import defaultdict as dd
inp=lambda :(int(o) for o in  stdin.readline().split())
sinp=lambda:(o for o in  stdin.readline().split())
out=lambda: stdout.write(str())
I=lambda:map(int,input().split())
Y=lambda:int(input())
#print(inp())    #generator object

for _ in range(int(input())):
    n,a,b=I()
    if 2*a<b:
        print(n*a)
    else:
        print((n//2)*b+(n%2)*a)
