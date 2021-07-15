n=int(input())
if n%2==0:
    print("NO")
else:
    n-=1
    n-=2
    jam=int(n//2)
    if jam>0:
        print(1,jam)
    else:
        print("NO")
