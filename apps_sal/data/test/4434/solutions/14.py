import math 
def ri():
    return map(int,input().split())
def li():
    return list(map(int,input().split()))
def inp():
    return int(input())
def si():
    return input()
def pYes():
    print("YES")
def pNo():
    print("NO")
def plist(l):
    print("".join(l))
t = int(input())
for i in range(t):
    n = int(input())
    ans=0
    t=1
    for k in range(3,n+1,2):
        
        ans+=(2*k + (k-2)*2)*t
        t=t+1
    print(ans)
