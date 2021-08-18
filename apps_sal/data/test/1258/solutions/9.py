from collections import defaultdict as dd
import sys
input = sys.stdin.readline
n = int(input())
l = []
cc = [0] * (n + 1)
d = dd(list)
res = []
one = []
two = []
for i in range(n - 2):
    a, b, c = map(int, input().split())
    l.append((a, b, c))
    cc[a] += 1
    cc[b] += 1
    cc[c] += 1
    d[a].append((a, b, c))
    d[b].append((a, b, c))
    d[c].append((a, b, c))
for i in range(len(cc)):
    if(cc[i] == 1):
        one.append(i)
    if(cc[i] == 2):
        two.append(i)
f = d[one[0]]
prev = [one[0]]
if(cc[f[0][0]] == 2):
    prev.append(f[0][0])
if(cc[f[0][1]] == 2):
    prev.append(f[0][1])
if(cc[f[0][2]] == 2):
    prev.append(f[0][2])
if(cc[f[0][0]] == 3):
    prev.append(f[0][0])
if(cc[f[0][1]] == 3):
    prev.append(f[0][1])
if(cc[f[0][2]] == 3):
    prev.append(f[0][2])
res.append(prev)
cur = []
k = n - 3
while k:
    for j in d[prev[1]]:
        if(prev[2] in j and prev[0] not in j):
            f = j
            break
    prev = [prev[1], prev[2]]
    for v in j:
        if(v != prev[0] and v != prev[1]):
            prev.append(v)
    res.append(prev)
    k -= 1
print(res[0][0], res[0][1], res[0][2], end=" ")
for i in range(1, len(res)):
    print(res[i][2], end=" ")
