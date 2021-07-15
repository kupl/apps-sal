l = [ list(map(int,input().split(" "))) for i in range(3)]
n=int(input())
for i in range(n):
    b=int(input())
    for j in range(3):
        for k in range(3):
            if l[j][k]==b:
                l[j][k]=-1
if l[0][0]==-1 and l[0][1]==-1 and l[0][2]==-1:
    print("Yes")
elif l[1][0]==-1 and l[1][1]==-1 and l[1][2]==-1:
    print("Yes")
elif l[2][0]==-1 and l[2][1]==-1 and l[2][2]==-1:
    print("Yes")
elif l[0][0]==-1 and l[1][0]==-1 and l[2][0]==-1:
    print("Yes")
elif l[0][1]==-1 and l[1][1]==-1 and l[2][1]==-1:
    print("Yes")
elif l[0][2]==-1 and l[1][2]==-1 and l[2][2]==-1:
    print("Yes")
elif l[0][0]==-1 and l[1][1]==-1 and l[2][2]==-1:
    print("Yes")
elif l[0][2]==-1 and l[1][1]==-1 and l[2][0]==-1:
    print("Yes")
else:
    print("No")

