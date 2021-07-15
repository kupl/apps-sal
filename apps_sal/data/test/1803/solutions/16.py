from sys import stdin

stdin.readline()
a = list()
a.append(0)
for x in stdin.readline().strip().split(): a.append(int(x))
a.append(0)
m = int(stdin.readline().strip())
for i in range(m):
    x,y = [ int(x) for x in stdin.readline().strip().split() ]
    a[x-1] += y-1
    a[x+1] += a[x]-y
    a[x] = 0
print('\n'.join([ str(x) for x in a[1:-1] ]))

    

