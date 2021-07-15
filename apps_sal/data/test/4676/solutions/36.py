o=input()
e=input()
s=[]
i=1
j=0
while True:
    if i%2==0:
        s.append(e[j])
        i+=1
        j+=1
    else:
        s.append(o[j])
        i+=1
    if i>=len(o)+len(e)+1:
        break
for i in range(len(s)):
    print(s[i],end="")
