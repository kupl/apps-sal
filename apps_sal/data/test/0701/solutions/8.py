s=input().strip()
t=input().strip()
i=0
j=0
while i<len(s) and j<len(t):
    if t[j]!=s[i]:
        i+=1
    else:
        i+=1
        j+=1
if j==len(t):
    print('automaton')
    return
c1=[0]*26
c2=[0]*26
for i in s:
    c1[ord(i)-ord('a')]+=1
for i in t:
    c2[ord(i)-ord('a')]+=1
boo=True
for i in range(26):
    if c1[i]>c2[i]:
        boo=False
    if c1[i]<c2[i]:
        print('need tree')
        return
if boo:
    print('array')
else:
    print('both')
