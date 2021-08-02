line = input()
d = {}
dist = {}
for i in range(len(line)):
    elem = line[i]
    if elem not in d:
        d[elem] = i
        dist[elem] = i + 1
    else:
        dist[elem] = max(dist[elem], i - d[elem])
        d[elem] = i
    # print(dist)
minimum = 999999999
for key in dist:
    dist[key] = max(dist[key], len(line) - d[key])
    minimum = min(minimum, dist[key])
print(minimum)
