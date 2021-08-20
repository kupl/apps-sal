gems = {'purple': 'Power', 'green': 'Time', 'blue': 'Space', 'orange': 'Soul', 'red': 'Reality', 'yellow': 'Mind'}
N = int(input())
arr = []
for i in range(N):
    del gems[input()]
print(len(gems))
for cols in gems:
    print(gems[cols])
