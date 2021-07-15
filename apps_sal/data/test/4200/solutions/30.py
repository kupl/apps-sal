n,m = list(map(int,input().split()))
a = list(map(int,input().split()))

st = sum(a) / (4*m)
a.sort(reverse = True)
el = a[:m]

for i in range(m):
    if el[i] < st:
        print('No')
        return

print('Yes')

