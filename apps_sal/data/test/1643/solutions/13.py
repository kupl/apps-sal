s = input()[::-1]
ans=''
c=0
for i in s:
    if i=='0':
        ans+='0'
        c+=1
    elif c>0:
        ans+='1'
        c-=1
    else:
        ans+='0'
print(ans[::-1])                

