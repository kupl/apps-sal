n=int(input())
c,o=0,0
for i in input():
    if i=='x':
        c+=1
    else:
        c=0
    if c>=3:
        o+=1
print(o)

