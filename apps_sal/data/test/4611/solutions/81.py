n=int(input())
bx=by=bt=0
ans='Yes'

for i in range(n):
    t,x,y=map(int, input().split())
    if t%2!=(x+y)%2:
        ans='No'
    if abs(bx-x)+abs(by-y)>abs(bt-t):
        ans='No'
    bx=x
    by=y
    bt=t

print(ans)
