w,h,x,y = map(int,input().split())

n = 0
if x == w/2 and y == h/2:
    n = 1

print(w*h/2,n)
