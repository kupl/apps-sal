n=input()
flag=0
for i in range(3):
    if n[i]=="7":
        flag=1
        break
if flag==0:
    print("No")
else:
    print("Yes")
