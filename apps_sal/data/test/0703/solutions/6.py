string=str(input())+' '
word=''
wordlist=[]
boxes=0

for char in string:
    if char!=' ':
        word+=char
    else:
        wordlist.append(int(word))
        word=''

maxsections=wordlist[0]
nuts=wordlist[1]
divisors=wordlist[2]
maxnuts=wordlist[3]

while nuts>0:
    boxes+=1
    
    if divisors>=maxsections-1:
        divisors-=maxsections-1
        if nuts>=maxsections*maxnuts:
            nuts-=maxsections*maxnuts
        elif nuts<maxsections*maxnuts:
            nuts=0

    elif divisors<maxsections-1:
        if nuts>=(divisors+1)*maxnuts:
            nuts-=(divisors+1)*maxnuts
        elif nuts<(divisors+1)*maxnuts:
            nuts=0
        divisors=0

print(boxes)

