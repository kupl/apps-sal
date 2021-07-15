w=input()
di={}
for i in w:
    if i in di:
        di[i]+=1
    else:
        di[i]=1
for i in di.values():
    if i&1:
        print("No")
        return
print("Yes")
