s = input()
f=[0]*26
a='a'
for ele in s:
    f[ord(ele)-ord(a)]+=1 

se = set(s)

if len(se) == 1 or len(se)>4: 
    print("No")
    return
if len(se)==2:
    s = list(se)
    if f[ord(s[0])-ord(a)]>1 and f[ord(s[1])-ord(a)]>1:
        print("Yes")
    else:
        print("No")
if len(se)==3:
    if f[ord(s[0])-ord(a)]>1 or f[ord(s[1])-ord(a)]>1 or f[ord(s[2])-ord(a)]>1:
        print("Yes")
    else:
        print("No")
if(len(se))==4:
    print("Yes")
