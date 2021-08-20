l = input().split()
n = int(l[0])
m = int(l[1])
l = []
for i in range(n):
    lo = input().split()
    l.append(int(lo[0]) * int(lo[1]))
hashi = dict()
for i in range(m):
    lo = input().split()
    z = int(lo[0]) * int(lo[1])
    if z in hashi:
        hashi[z] += 1
    else:
        hashi[z] = 1
count = 0
for i in range(n):
    if l[i] in hashi and hashi[l[i]] > 0:
        count += 1
        hashi[l[i]] -= 1
print(count)
