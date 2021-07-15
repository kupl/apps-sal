from decimal import *
getcontext().prec = 50
n = int(input())
inputs= list(map(int,input().split()))
inputs1= list(map(int,input().split()))
dic={
}
temp=0
for i in range(len(inputs)):
    if inputs[i]==0 and inputs1[i]!=0:
        continue
    elif inputs[i]==0 and inputs1[i]==0:
        temp+=1
        continue

    c=-Decimal(inputs1[i])/Decimal(inputs[i])
    if c in list(dic.keys()):
        dic[c]+=1
    else:
        dic[c]=1
if len(dic)>0:
    print(max(dic.values())+temp)
else:
    print(0+temp)

