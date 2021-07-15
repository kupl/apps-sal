N=int(input())
for i in range((N-1)//4+2):
    if (N-4*i)%7==0:
        print("Yes")
        break
else:
    print("No")

