s=input()
a=""
for i in range(len(s)):
    if s[i]=="0":
        a+="0"
    elif s[i]=="1":
        a+="1"
    else:
        if a!="":
            a=a[:-1]
print(a)
