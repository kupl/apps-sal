(n, k) = [int(x) for x in input().strip().split(' ')]
dataF = input().strip().split(' ')
dataF = [int(x) for x in dataF]
data = [0]
for i in range(len(dataF)):
    if data[len(data) - 1] != dataF[i]:
        data.append(dataF[i])
data = data[1:]
res = {x: 0 for x in set(data)}
res[data[0]] += 1
res[data[len(data) - 1]] += 1
for i in range(0, len(data) - 2, 1):
    prev = data[i]
    curr = data[i + 1]
    next = data[i + 2]
    if prev == next:
        res[curr] += 2
    if prev != next:
        res[curr] += 1
print(max(res, key=res.get))
