n,m = list(map(int,input().split()))
a = list(map(int,input().split()))

s = sum(a)
a.sort(reverse=True)
el = a[:m]


for i in el:
    if i < s*(1/(4*m)):
        print('No')
        return
print('Yes')

