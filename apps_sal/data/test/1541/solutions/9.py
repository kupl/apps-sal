a = input().strip()
n= len(a)
c = a.index('^')
l,r = 0,0
for i in range(c):
    if a[i].isdigit():
        l+=(c-i)*int(a[i])
for i in range(c+1,n):
    if a[i].isdigit():
        r+=(i-c)*int(a[i])
if l==r:
    print('balance')
elif l>r:
    print('left')
else:
    print('right')

