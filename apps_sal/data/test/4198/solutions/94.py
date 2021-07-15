a,b,x = map(int, input().split())

mn = 0
mx = 10**18

while mn+1 < mx :
    mid = (mn + mx) //2
    price = a*mid + b*len(str(mid))
    if(price <= x):
        mn = mid
    else :
        mx = mid
    
if(mid >= 10**9):
    print(10**9)
else :
    print(mn)
