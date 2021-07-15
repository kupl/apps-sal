radi=input()
list=radi.split(" ")
N=int(list[0])
K=int(list[1])
empty=""
for items in range(K):
    koyjon=input()
    empty+=input()+" "
new=empty.split()
emp=[]
for i in new:
    if i not in emp:
        emp.append(i)
print((N-len(emp)))



