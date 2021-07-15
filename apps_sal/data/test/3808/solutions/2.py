n=int(input())
s=input()
if s.count('(')!=s.count(')'):
    print('No')
    return 
stk=[] 
karma=0 
f=1 
ans=1 
for i in s:
    if i=='(': 
        stk.append(i)
    else:
        if not stk:
            f=0 
            if not karma: 
                karma=1 
            else:
                ans=0 
                break 
        else:
            stk.pop() 
if ans and len(stk)==1 and stk[0]=='(':
    print('Yes')
    return 
if not stk and f :
    f=1 
if f:
    print('Yes')
    return 
if not ans:
    print('No')
    return
