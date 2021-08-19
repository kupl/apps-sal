n = int(input())
d = {'purple': 'Power', 'green': 'Time', 'blue': 'Space', 'orange': 'Soul', 'red': 'Reality', 'yellow': 'Mind'}
for i in range(n):
    s = input()
    del d[s]
print(len(d))
for k in d:
    print(d[k])
