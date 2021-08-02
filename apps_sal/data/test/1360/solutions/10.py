n = int(input())
v = list()
for i in range(n):
    v.append(list(int(x) for x in input().split()))

v.sort()
print
lastb = 0
for i in range(n):
    if (v[i][1] < v[i][0]) and (v[i][1] >= lastb):
        lastb = v[i][1]
    else:
        lastb = v[i][0]
print(lastb)
