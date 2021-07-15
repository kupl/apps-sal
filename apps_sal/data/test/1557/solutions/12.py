h1,a1,c1=map(int,input().split())
h2,a2=map(int,input().split())
a=list()
n=0
while h2>0:
    n+=1
    if (h1<(a2+1)) and (h2>a1):
        a.append('HEAL')
        h1+=c1
    else:
        a.append('STRIKE')
        h2-=a1
    h1-=a2
print(n)
for i in a:
    print(i)
