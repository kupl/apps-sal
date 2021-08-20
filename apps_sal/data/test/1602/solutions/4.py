n = int(input())
a = list(map(int, input().split()))
lis = [0] * 31
for i in a:
    for j in range(31):
        if i & 2 ** j > 0:
            lis[j] += 1
nmax = 0
maxind = 0
for (ind, i) in enumerate(a):
    for j in range(31):
        if lis[j] >= 2:
            i |= 2 ** j
            i -= 2 ** j
    if nmax < i:
        nmax = i
        maxind = ind
ans = [a[maxind]]
for i in range(n):
    if i != maxind:
        ans.append(a[i])
print(' '.join(map(str, ans)))
