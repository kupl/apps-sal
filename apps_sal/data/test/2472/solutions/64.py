import sys

n=int(input())
ba=[[0]*2 for i in range(n)]
for i in range(n):
    ai,bi=map(int,input().split())
    ba[i]=[bi,ai]
    
ba.sort() 

t=0
for i in range(n):
    t+=ba[i][1]
    if t>ba[i][0]:
        print("No")
        return
print("Yes") 
