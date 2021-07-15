S=input()
s=[]
total=0
for i in range(len(S)):
    s.append(int(S[i]))
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        total+=1
        s[i+1]=abs(1-s[i])
print(total)
