n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

c = [0]*n
d = [0]*k
t = list(range(1,n+1))

for i in range(n):
    if c[a[i]-1] < b[i]:
        c[a[i]-1] = b[i]
        d[a[i]-1] = t[i]

rp = list(set(t)-set(d))
t2 = [0]*len(rp)
for i in range(len(rp)):
    t2[i] = b[rp[i] - 1]

t2.sort()
rj = d.count(0)
s = sum(t2[:rj])

print(s)
