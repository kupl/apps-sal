import sys, math
s=input()
h=0
while h<len(s) and s[h]=='0':
    h+=1
s=s[h:]
if '.' in s and s[-1]=='0':
    g=1
    while g<=len(s) and s[-g]=='0':
        g+=1
    s=s[:(-g+1)]
if len(s)==0:
    print(0)
    return
idx=-1
for i in range(len(s)):
    if s[i]=='.':
        idx=i
        break
if idx==-1:
    idx=len(s)
else:
    if s[0]=='.':
        h=1
        while h<len(s) and s[h]=='0':
            idx-=1
            h+=1
if 1:
    mul = idx - 1
    
    new=''
    for i in range(len(s)):
        if s[i]!='.':
            new+=s[i]
    s=new
    if len(s) > 0 and s[-1]=='0':
        h=2
        while h<=len(s) and s[-h]=='0':
            h+=1
        s=s[:(-h+1)]
    if len(s) > 0 and s[0]=='0':
        h=1
        while h<len(s) and s[h]=='0':
            h+=1
        s=s[h:]
    mul=str(mul)
    if len(s)==0:
        print(0)
        return
    elif len(s)==1:
        print(s[0],end='')
        if mul != '0':
            print('E'+mul)
        return
    else:
        print(s[0]+'.'+s[1:],end='')
        if mul != '0':
            print('E'+mul)
        
        
            
    
            
    
        

