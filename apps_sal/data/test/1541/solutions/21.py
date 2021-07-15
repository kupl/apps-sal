s=input().strip()
l=0
r=0
for i in range(len(s)):
    if s[i]=='^': p=i
for i in range(len(s)):
    if '1'<=s[i]<='9':
        if i>p:
            r+=int(s[i])*(i-p)
        else:
            l+=int(s[i])*(p-i)
if l>r:
    print('left')
elif l==r:
    print('balance')
else:
    print('right')
