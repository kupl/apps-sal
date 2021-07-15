n=int(input())
if (n % 2 == 0):
    print("No")
else:
    a=list(map(int,input().split()))
    if (a[0]%2 == 0):
        print("No")
    else:
        if a[n-1] % 2 == 0:
            print("No")
        else:
            print("Yes")

