A,B=list(map(int,input().split()))
if abs(A-B)%2==0:
    print(((A+B)//2))
else:
    print("IMPOSSIBLE")

