O = input()
E = input()

combi=''

for i in range(len(O)+len(E)):
    if i%2==0:
        combi+=O[i//2]
    elif i%2!=2:
        combi+=E[i//2]
print(combi)
