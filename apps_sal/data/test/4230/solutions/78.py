x,n = map(int, input().split())
p = list(map(int, input().split()))

l = [i for i in range(102)]

for j in p:
    l.remove(j)

m = []

for k in l:
    m.append(abs(k-x))

print(l[m.index(min(m))])
