s=list(map(int,input()))
stack=[]
for i in range(len(s)):
    if s[i]==1:
        stack.append(i)
    elif len(stack)!=0:
        stack.pop()
for i in stack:
    s[i]=0
s=list(map(str,s))
print(''.join(s))

