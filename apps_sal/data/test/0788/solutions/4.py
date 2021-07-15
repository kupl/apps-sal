s=input()
f=0
c=0
for i in range(1,6):
    if s[i:i+2]=='10':
        c+=10
    else:
        c+=int(s[i])
    #print(s[i:i + 2],c,i)
if(s[6]!='0'):
    c+=int(s[6])
print(c+1)

