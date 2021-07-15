a=int(input())
i=1
li=[a]
import copy
while True:
    if li[i-1]%2==0:
        b=li[i-1]//2
    else:
        b=3*li[i-1]+1
    if b in li:
        print((i+1))
        return
    li.append(b)
    i+=1
        

