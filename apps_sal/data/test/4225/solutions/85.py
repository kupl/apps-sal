a,b,c,k = map(int,input().split())
if a >= k :
    print(k)
elif a+ b >= k:
    print(a)
else:
    print(2*a + b - k)
