n = int(input())
arr = []
d = {}
for i in range(n - 2):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])
    d[a] = d.get(a, []) + [i]
    d[b] = d.get(b, []) + [i]
    d[c] = d.get(c, []) + [i]
# print(d)
for i in d:
    if len(d[i]) == 1:
        ind = d[i][0]

vis = [0] * (n - 2)
visno = [0] * (n + 1)
q = [arr[ind]]
vis[ind] = 1
# print(d)
# print(arr)
if len(d[q[0][0]]) == 1:
    print(q[0][0], end=" ")
    visno[q[0][0]] = 1


elif len(d[q[0][1]]) == 1:
    print(q[0][1], end=" ")
    visno[q[0][1]] = 1

else:
    print(q[0][2], end=" ")
    visno[q[0][2]] = 1

# print(q)

if len(d[q[0][0]]) == 2:
    print(q[0][0], end=" ")
    visno[q[0][0]] = 1
    prev = q[0][0]
    if len(d[q[0][0]]) == 2:
        for i in (d[q[0][0]]):
            if vis[i] == 0:
                q.append(arr[i])
                vis[i] = 1


elif len(d[q[0][1]]) == 2:
    print(q[0][1], end=" ")
    visno[q[0][1]] = 1
    prev = q[0][1]
    if len(d[q[0][1]]) == 2:
        for i in (d[q[0][1]]):
            if vis[i] == 0:
                q.append(arr[i])
                vis[i] = 1

else:
    print(q[0][2], end=" ")
    visno[q[0][2]] = 1
    prev = q[0][2]
    if len(d[q[0][2]]) == 2:
        for i in (d[q[0][2]]):
            if vis[i] == 0:
                q.append(arr[i])
                vis[i] = 1
# q.pop(0)
# print(q)
for i in range(n - 4):
    p = q.pop(0)
    for j in p:
        if visno[j] == 0:
            visno[j] = 1
            for k in d[j]:
                if vis[k] == 0:
                    vis[k] = 1
                    q.append(arr[k])
                    print(j, end=" ")
                    break
            break
q.pop(0)
# print(q)
for j in q[0]:
    if len(d[j]) == 2:
        print(j, end=" ")

for j in q[0]:
    if len(d[j]) == 1:
        print(j, end=" ")

# for i in range()
