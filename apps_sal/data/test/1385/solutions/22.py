n=input()
z,i=len(n),0
while i<z:
    if n[i]=='"':
        k="<";i+=1
        while i<z and n[i]!='"':k+=n[i];i+=1
        k+='>';i+=1
        print(k)
    elif n[i]!=" ":
        k="<"
        while i<z and n[i]!=" ":k+=n[i];i+=1
        k+=">"
        print(k)
    else:i+=1
