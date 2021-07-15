m=input()
n = len(m)
k,o=0,0
for i in range(n):
    if m[i]=='^':
        l=i
for i in range(l):
    if m[i].isdigit():
        k+=int(m[i])*(l-i)
for i in range(l,n):
    if m[i].isdigit():
        o+=int(m[i])*(i-l)        
if k==o:
    print('balance')
elif k>o:
    print('left')
else:
    print('right')

