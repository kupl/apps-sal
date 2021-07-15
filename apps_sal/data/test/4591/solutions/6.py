a,b,c,X,Y = map(int,input().split())

min1 = 10**10
for z in range(0,200001,2):
    x = max(0,X-z//2)
    y = max(0,Y-z//2)
    min1 = min(min1,a*x + b*y + c*z)

print(min1)
