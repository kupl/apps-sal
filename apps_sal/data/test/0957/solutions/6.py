x=input()
y="heidi"
z=""
j=0
for i in y:
    t=True
    while j<len(x) and t:
        if x[j]==i:
            z+=i
            t=False
        j+=1
else:
    if y==z:
        print("YES")
    else:
        print("NO")
