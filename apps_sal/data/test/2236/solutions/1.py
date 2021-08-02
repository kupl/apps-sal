d = {}
n = int(input())
l = list(map(int, input().split(' ')))
k = [l[0]]
d[l[0]] = 0
for i in range(1, n):
    k.append(k[-1] + l[i])
    d[k[-1]] = 0;
maxx = -1
for i in k:
    d[i] += 1
    maxx = max(maxx, d[i])
print(n - maxx)
