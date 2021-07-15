a=int(input())
b=input()
c=[]
k=1
for i in range(a):
    if b[i]=='R' and 'L' in c or b[i]=='L' and 'R' in c or b[i]=='U' and 'D' in c or b[i]=='D' and 'U' in c:
        c=[]
        k+=1
        c.append(b[i])
    if not b[i] in c:
        c.append(b[i])
print(k)
