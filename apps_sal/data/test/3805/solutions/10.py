import sys
import math
 
st = input()
mystack = [st[0]]

for i in range(1, len(st)):
    if(mystack != []):
        v = mystack.pop()
        if(v != st[i]):
            mystack.append(v)
            mystack.append(st[i])
    else:
        mystack.append(st[i])

if(mystack == []):
    print("Yes")
else:
    print("No")
