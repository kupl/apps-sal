n = int(input())
ar = []
for i in range(n):
    s = input()
    if s == 'purple':
        ar.append('Power')
    if s == 'green':
        ar.append('Time')
    if s == 'blue':
        ar.append('Space')
    if s == 'orange':
        ar.append('Soul')
    if s == 'red':
        ar.append('Reality')
    if s == 'yellow':
        ar.append('Mind')
ans = ['Mind', 'Reality', 'Soul', 'Space', 'Time', 'Power']
a = []
for x in ans:
    if x in ar:
        continue
    a.append(x)
print(len(a))
for x in a:
    print(x)
