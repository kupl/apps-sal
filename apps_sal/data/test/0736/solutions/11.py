'''
Created on Oct 12, 2014

@author: Ismael
'''
ok = False
n,m = map(int,input().split())
for y in range(n//2,-1,-1):
    if((n-y)%m==0):
        print(y+(n-2*y))
        ok = True
        break
if(not ok):
    print(-1)
