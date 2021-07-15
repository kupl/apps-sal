n,k = map(int,input().split(' '))
s1 = input()
m = list(set(s1))
m = sorted(m)
D = {}
for i in range(len(m)):
    D[m[i]] = i
X = len(D)
if len(s1)<k:
    print(s1+m[0]*(k-len(s1)))
else:
    st = list(s1[0:k])
    st = [D[i] for i in st]
    f = k-1
    st[f]+=1
    while st[f]==X:
        st[f]=0
        st[f-1]+=1
        f-=1
    st = [m[i] for i in st]
    print(''.join(st))
