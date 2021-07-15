n = int(input())
a = list(map(int, input().split()))

nmax = max(a)
target = nmax/2

cur = a[0] if a[0] != nmax else a[1]
curdiff = abs(cur-target)

for i in range(n):
    if a[i] == nmax:
        continue

    diff = abs(a[i]-target)

    if diff < curdiff:
        curdiff = diff
        cur = a[i]

print(nmax, cur)
