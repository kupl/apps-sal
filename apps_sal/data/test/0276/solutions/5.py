n = int(input())
a = {'Power', 'Time', 'Space', 'Soul', 'Reality', 'Mind'}
for i in range(n):
    s = input()
    if s == 'red':
        a.remove('Reality')
    elif s == 'purple':
        a.remove('Power')
    elif s == 'green':
        a.remove('Time')
    elif s == 'blue':
        a.remove('Space')
    elif s == 'orange':
        a.remove('Soul')
    elif s == 'yellow':
        a.remove('Mind')
print(len(a))
for i in a:
    print(i)
