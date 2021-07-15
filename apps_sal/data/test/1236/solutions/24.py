n,m=map(int,input().strip().split())
a=list(map(int,input().strip().split()))
x=0
for i in range(n):
    if (a[i]&1):
        x=x+1
# print(x)
if (n==m):
    if (x&1):
        print("Stannis")
    else:
        print("Daenerys")
elif ((n-m)&1):
    if (m&1):
        if ((n-m)//2>=x):
            print("Daenerys");
        else:
            print("Stannis");
    else:
        if ((n-m)//2>=x or (n-m)//2>=(n-x)):
            print("Daenerys")
        else:
            print("Stannis");
else:
    if (m&1):
        if ((n-m)//2>=(n-x)):
            print("Stannis")
        else:
            print("Daenerys")
    else:
        print("Daenerys")
