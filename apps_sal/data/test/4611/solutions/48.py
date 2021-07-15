N = int(input())
t,x,y = 0,0,0
for i in range(N):
    a,b,c = t,x,y
    t,x,y = map(int,input().split())
    d = abs(x-b)+abs(y-c)
    e = t-a
    if d%2 != e%2 or d > e:
        print("No")
        return
print("Yes")
