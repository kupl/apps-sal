n=int(input())

encode1=''.join(['<3'+input() for i in range(n)])+'<3'

encode2=input()

i=0
j=0
while i<len(encode1) and j<len(encode2):
    if(encode1[i] == encode2[j]):
        i+=1
        j+=1
    else:
        t=encode2[j]
        if not (('z'>=t and t>='a') or ('9'>=t and t>='0') or t=='>' or t=='<'):
            i=999999
            j=999999
        j+=1

if i==len(encode1):
    print('yes')
else:
    print('no')

