A=input()
nu=int(A)
tmp=sum(map(int,list(A)))
print("Yes") if nu%tmp==0 else print("No")
