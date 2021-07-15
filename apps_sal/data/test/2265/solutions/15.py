a=input()
b=input()
A=[]
al=len(a)
bl=len(b)
A.append(0)
count=0
for x in a:
    if x=='1':
        count+=1
    A.append(count)
evencount=0
bcount=0
for x in b:
    if x=='1':
        bcount+=1
for i in range((al+1)-bl):
    acount=A[i+bl]-A[i]
    if (acount%2)==(bcount%2):
        evencount+=1
print(evencount)

