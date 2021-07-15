n, m, k = [int(x) for x in input().split()]
a = []
for i in range(m):
    a.append([0] * n)
for i in range(n):
    t = input().split()
    for j in range(m):
        a[j][i] = int(t[j])
maxs = 0
r = 0
for i in a:
    maxframe = 0
    mfp = -1
    for j in range(n - k + 1):
        if sum(i[j:j + k]) > maxframe:
            maxframe = sum(i[j:j + k])
            mfp = j
    maxs += maxframe
    r += sum(i[:mfp])
print(maxs, r)
