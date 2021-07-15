import operator
data = list( map (int, input().split(' ')) )
n = data[0]
m = data[1]
edge = {}
for i in range(n):
    edge[i+1] = []
for _ in range(m):
    data = list( map (int, input().split(' ')) )
    i = data[0]
    j = data[1]
    edge[i].append(j)
    edge[j].append(i)
candidate = [k for k,v in list(edge.items()) if len(v) == 2]
result = 0
used = {}
def _iscircle(c, result):
    n = edge[c][0]
    used[c] = 1
    last = c
    while n not in used:
        used[n] = 1
        if len(edge[n]) != 2:
            return result
        t = edge[n][0]
        if t != last:
            last = n
            if t == c:
                return result + 1
            n = t
            continue
        last = n

        t = edge[n][1]
        if t == c:
            return result + 1
        n = t
    return result


for i in candidate:
    result = _iscircle(i, result)
print (result)

