def remove():
    nonlocal c,tot,s
    c+=1
    if not s:   return
    elif s.pop()==c-1:  return
    tot,s=tot+1,[]
s,tot,c=[],0,1
for _ in range(int(input())*2):
    cmd= list(input().split())
    if cmd[0]=='add':
        s.append(int(cmd[1]))
    else:   remove()
print(tot)

