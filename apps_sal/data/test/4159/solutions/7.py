a,b,k = map(int,input().split())

if a >= k:
    a -=k
    print(a,b)
    return
else:
    k -=a
    a = 0
    
if b >= k:
    b -=k
    print(a,b)
    return
else:
    b = 0

print(a,b)
