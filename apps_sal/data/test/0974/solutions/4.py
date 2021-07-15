n=int(input())
mas=[]
p=0
r=0
for i in range(2*n):
    s=input().split()
    if s[0]=='add':
       mas.append(int(s[1]))
    else:
        r += 1
        if len(mas)>0 and r==mas[-1]:
            del mas[-1]
        elif len(mas)>0:
            p+=1
            mas=[]
print(p)
