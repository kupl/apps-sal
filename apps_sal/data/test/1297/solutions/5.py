s=input()
Pred=''
C=0
D=0
for i in s:
    if i==Pred:
        C+=1
    if i!=Pred:
        if C%2==0 and C!=0:  D+=1
        C=1
        Pred=i
if C%2==0 and C!=0:  D+=1
print(D)
