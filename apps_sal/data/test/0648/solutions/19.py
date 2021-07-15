def fn(y,m,b):
    x=m*(b-y)
    ans=(x+1)*(y+1)*(x+y)
    return ans//2
m,b=list(map(int,input().split()))
lo=0
hi=b
while lo<hi:
    mid=(lo+hi)//2
    if fn(mid,m,b)>fn(mid-1,m,b) and fn(mid+1,m,b)>fn(mid,m,b):
        lo=mid
    elif fn(mid,m,b)<fn(mid-1,m,b) and fn(mid+1,m,b)<fn(mid,m,b):
        hi=mid
    else:
        break
print(fn(mid,m,b))



