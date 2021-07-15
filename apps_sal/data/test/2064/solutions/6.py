n = int(input())
if (n%2!=0):
    print(7,end="")
    for i in range(1,int(n/2)):
        print(1,end = "")
else:
     for i in range(0,int(n/2)):
        print(1,end = "")
