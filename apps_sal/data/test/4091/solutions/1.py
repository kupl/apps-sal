n,k = map(int,input().split())
l = list(map(int,input().split()))

l = sorted([(x,i) for i,x in enumerate(l)],key = lambda x: (x[0],x[1]))
used = l[-k:]

s = sum(x[0] for x in used)
days = sorted(x[1] for x in used)
print (s)

d = []
t = 0
for x in days[:-1]:
    d.append(x-t + 1)
    t = x + 1
d.append(n-t)
print (*d)
