s = input()

s1 = int(s[0]+s[1])
s2 = int(s[2]+s[3])
#print(s1, s2)
L=[]

for i in range(1, 13):
    L.append(i)


if s1 not in L and s2 not in L:
    print('NA')
elif s1 in L and s2 not in L:
    print('MMYY')
elif s1 not in L and s2 in L:
    print('YYMM')
else:
    print('AMBIGUOUS')

