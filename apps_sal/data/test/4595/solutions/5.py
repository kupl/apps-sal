s=input()
S=len(s)
mi=[]
ma=[]
for i in range(S):
    if s[i]=='A':
        mi.append(i)
    elif s[i]=='Z':
        ma.append(i)
print(max(ma)-min(mi)+1)
