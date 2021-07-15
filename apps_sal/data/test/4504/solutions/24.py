s=input()
m=0
if s[0]==s[1]:
    m=1
for i in range(1,len(s)//2):
    if i==len(s)//2-1:
        break
    if s[:i]==s[i:2*i]:
        m=i
print(2*m)
