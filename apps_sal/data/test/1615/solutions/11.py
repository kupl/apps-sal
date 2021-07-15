a=input().split(' ')
lista=[]
contador=0
contador2=0
for i in range(0,int(a[0])):
    b=input().split(' ')
    lista.append(b)
for j in range(0,len(lista)):
    contador+=int(lista[j][0])
    contador2+=int(lista[j][1])

formula=((contador-int(a[0]))-contador2)%int(a[-1])
print(formula)


