s,t=input().split()
a,b=map(int,input().split())
u=input()
print(*(a-1,b) if s==u else (a,b-1))
