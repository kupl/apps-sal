n = int(input())
l = []
stack = []
for i in range(n):
    d, s = map(int, input().split())
    if d == 1:
        stack.append(i)
    l.append([d, s])
c = 0
edges = ''
while stack:
    i = stack.pop(0)
    d, s = l[i]
    if d == 0:
        continue
    dd, ss = l[s]
    if dd == 2:
        stack.append(s)
    l[s] = [dd - 1, ss ^ i]
    edges += str(i) + ' ' + str(s) + '\n'
    c += 1
print(c)
print(edges)
