a,b,c=map(int,input().split())
print("Lucky Chef") if ((c-a)//b)%2==0 else print("Unlucky Chef")
