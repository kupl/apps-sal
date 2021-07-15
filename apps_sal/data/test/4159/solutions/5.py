a,b,k = map(int,input().split())
if k >= a:
    k -= a
    a = 0
    b -= k
else:
    a -= k
print(a,max(0,b))
