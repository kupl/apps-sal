w,h,x,y= map(int, input().split())

if x==w/2 and y==h/2:
    ans='1'
else:
    ans='0'

print(w*h/2,ans)
