n = int(input())
x = [int(i) for i in input().split()]
data = dict()
for i in range(0, n):
    if not x[i] in data:
        data[x[i]] = [1, i]
    else:
        data[x[i]] = [data[x[i]][0] + 1, i]
t = list(data.items())
t.sort(key=lambda x: (-x[1][0], x[1][1]))
print(t[0][0])
