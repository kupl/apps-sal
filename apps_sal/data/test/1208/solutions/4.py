n = int(input())
col = 0
max = 0
p = []
q = []
e = []
for i in range(n):
    a, b = list(input().split())
    b = int(b)
    q.append([a, b])
    if a == '-' and b not in p:
        col += 1
        e.append(b)
    p.append(b)
for i in range(n):
    if col >= max:
        max = col
    if q[i][0] == '+':
        e.append(q[i][1])
        col += 1
    else:
        e.remove(q[i][1])
        col -= 1
    if col >= max:
        max = col
print(max)
