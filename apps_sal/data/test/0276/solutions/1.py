n = int(input())
names = []
for _ in range(n):
    names.append(input().strip())
names = set(names)
stones = {'purple': 'Power', 'green': 'Time', 'blue': 'Space', 'orange': 'Soul', 'red': 'Reality', 'yellow': 'Mind'}
missing = set(stones.keys()) - names
print(len(missing))
print('\n'.join((stones[v] for v in missing)))
