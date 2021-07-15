a, b = map(int, input().split(' '))
x=list(map(int, input().split(' ')))
s = sum(x)
t = []
for i in range(a):
    minx = b-(a-1)
    maxx = b-(s - x[i])
    xx = 0
    if min(minx, maxx)>0:
        xx += (min(minx, maxx)-1)
    
    if max(minx, maxx)<x[i]:
        xx += x[i] - (max(minx, maxx))
    t.append(xx)
print(' '.join([str(x) for x in t]))
