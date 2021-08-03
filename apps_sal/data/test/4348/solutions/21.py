n, k = list(map(int, input().strip().split()))
r = input()
r1 = "abcdefghijklmnopqrstuvwxyz"
l = [[] for i in range(26)]
d = {}
for u1 in range(26):
    d[r1[u1]] = u1
for t in range(n):
    l[d[r[t]]].append(t)
l1 = []
for x in l:
    for y in x:
        l1.append(y)
s = ""
l2 = []
for o in range(k, n):
    l2.append(l1[o])
l2.sort()
for i in l2:
    s = s + r[i]
print(s)
