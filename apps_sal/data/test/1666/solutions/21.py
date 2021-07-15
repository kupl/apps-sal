entrada = list([int(x) for x in input().split()])
qtdjogadasVencedor = entrada[0]#3
qtdjogadasPerdedor = entrada[1]#2
qtdminpontVencedor = entrada[2]#1
qtdminpontPerdedor = entrada[3]#1
listaPrincipal, laux = [], []
for i in range(qtdminpontVencedor,qtdjogadasVencedor+1):
    for j in range(qtdminpontPerdedor,qtdjogadasPerdedor+1):
        if j < i:
            laux.append((i,j))
print(len(laux))
for i in laux:
    print(i[0],i[1])
        
        

