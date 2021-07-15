sa=int(input())
print(int((sa**2+1)/2))
for x in range(sa):
    newchain=''
    if x%2==0:
        while len(newchain)<sa:
            if len(newchain)<sa:
                newchain+='C'
            if len(newchain)<sa:
                newchain+='.'
    if x%2==1:
        while len(newchain)<sa:
            if len(newchain)<sa:
                newchain+='.'
            if len(newchain)<sa:
                newchain+='C'

    print(newchain)
