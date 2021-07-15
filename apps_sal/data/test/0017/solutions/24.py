n,t,k = map(int,input().split())

if(t>k):
    print(k)
elif(k>n):
    print(t-(k-n))
else:
    print(t)
