s=input()
fin=""
for c in s:
    if c=='1':
        fin+="1"
    elif c=='0':
        fin+="0"
    else:
        if len(fin)>0:
            fin=fin[:-1]
print(fin)

