from math import inf
n = int(input())
s = [int(e) for e in input().split()]
c = [int(e) for e in input().split()]
d = [[inf, inf] for i in range(n)]
for i in range(n):
    s1 = s[i]
    for j in range(i):
        if s[j] < s1:
            if c[j] < d[i][0]:
                d[i][0] = c[j]
            if d[j][0] < d[i][1]:
                d[i][1] = d[j][0]
    d[i][0] += c[i]
    d[i][1] += c[i]
m = min([e[1] for e in d])
print(m if m < inf else -1)
