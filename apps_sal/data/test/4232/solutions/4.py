n, k = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]
d = {}
for i in range(n):
    if s[i] not in d:
        d[s[i]] = 1
    else:
        d[s[i]] += 1
q = []
for i in d:
    q.append((i, d[i]))
q.sort()
# print(q)
l = 0
if k == 0:
    if q[0][0] == 1:
        print(-1)
        return
    else:
        print(q[0][0] - 1)
        return
    
for i in range(len(d)):
    l += q[i][1]
    if l == k:
        print(q[i][0])
        return
print(-1)


