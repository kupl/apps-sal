s=input()
s=s.replace('eraser','*')
s=s.replace('erase','*')
s=s.replace("dreamer","*")
s=s.replace("dream","*")
f=1
for i in s:
    if i!='*':
        f=0
        break
if f:
    print("YES")
else:
    print("NO")

