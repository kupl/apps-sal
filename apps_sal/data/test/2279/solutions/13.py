from collections import defaultdict
n = int(input())
d = defaultdict()
t = 0
b = []
c = []
aa = [0] * ((2 * n) + 1)
while t < 2 * n - 1:
   # print(t)
    a = [int(x) for x in input().split()]
    for i in range(len(a)):
        d[a[i]] = [t + 2, i + 1]
    t = t + 1
l = sorted(d.items())
# print(l)
i = len(l) - 1
k = 0
while i >= 0:

    if aa[l[i][1][0]] == 0 and aa[l[i][1][1]] == 0:
        aa[l[i][1][0]] = l[i][1][1]
        aa[l[i][1][1]] = l[i][1][0]
        k = k + 2
        if k == (2 * n):
            break
        # print(aa)
    i = i - 1
for i in range(1, (2 * n) + 1):
    print(aa[i], end=" ")
