n=int(input())
pari=[]
dispari=[]
for _ in range(n):
    appo=int(input())
    if appo%2==0:
        pari.append(appo)
    else:
        dispari.append(appo)
diz={}
for i in range(len(pari)-1):
    for j in range(i+1, len(pari)):
        diz[(pari[i]+pari[j])>>1]=1 
for i in range(len(dispari)-1):
    for j in range(i+1, len(dispari)):
        diz[(dispari[i]+dispari[j])>>1]=1 
counter=0
for el in pari:
    if el in diz:
        counter+=1
for el in dispari:
    if el in diz:
        counter+=1
print(counter)
