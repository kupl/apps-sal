n = int(input())

jog = [int(i) for i in input().split()]
mi = min(jog)

qtd = 0
for i in range(len(jog)):
    if(jog[i] == mi):
        qtd+=1
if(qtd <= n//2 and qtd!=0):
    print("Alice")
else:
    print("Bob")

