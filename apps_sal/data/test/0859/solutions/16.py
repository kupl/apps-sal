def ans(p, k):
    nonlocal d
    if k == n:
        d.append(p)
        return
    ans(p+1, k+1)
    ans(p-1, k+1)
    return

s1 = input()
s2 = input()
b = 0
k = 0
d = []

for i in s1:
    if i == '+':
        b+=1
    else:
        b-=1
for i in s2:
    if i == '+':
        b-=1
    elif i == '-':
        b+=1
    else:
        k+=1
        
n = k
ans(0,0)
#print(d)
s=0
for i in d:
    if i == b:
        s+=1

#c = (k-abs(b))/2
#print(c)
#g=f[k-1]/f[k-int(c)-1]/2
#print(g)
if b > k:
    print('%.9f' % 0)
elif b == k:
    print('%.9f' % (1/(2**(k))))
elif (k - b) % 2 == 0:
    print('%.9f' % (s/(2**(k))))
else:
    print('%.9f' % 0)
