mp = {
    'purple': 'Power',
    'green': 'Time',
    'blue': 'Space',
    'orange': 'Soul',
    'red': 'Reality',
    'yellow': 'Mind',
}
n = int(input())
L = ['Power', 'Time', 'Space', 'Soul', 'Reality', 'Mind']
for _ in range(n):
    co = input().strip()
    L.remove(mp[co])
print(len(L))
for x in L:
    print(x)
