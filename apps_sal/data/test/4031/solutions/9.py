n=int(input())
s=[]
for x in range(n):
    e=input()
    s.append(e)
s=sorted(s,key=lambda x:len(x))
def issubstring(a,b):
    return b.count(a)
b=True
for x in range(n):
    for y in range(x):
        if(not issubstring(s[y],s[x])):
            b=False
if b:
    print("YES")
    for x in s:
        print(x)
else:
    print("NO")
