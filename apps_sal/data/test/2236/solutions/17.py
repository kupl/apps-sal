n = int(input(''))
l = input('').split(' ')
for i in range(len(l)):
    l[i] = int(l[i])
s = 0
m = 0
ps = {}
for i in range(len(l)):
    s += l[i]
    if s in ps:
        ps[s] += 1
    else:
        ps[s] = 1
    if ps[s] > m:
        m = ps[s]
print(n - m)
