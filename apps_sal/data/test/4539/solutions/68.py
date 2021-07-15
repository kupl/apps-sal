S=input()
N=int(S)
f=sum(int(x) for x in S)
if N%f==0:
    print("Yes")
else:
    print("No")

