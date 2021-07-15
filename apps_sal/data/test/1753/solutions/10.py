n, m = map(int, input().split())
a = [[] for i in range(n + 1)]
for i in range(m):
    loc1, loc2 = map(int, input().split())
    a[loc1].append(loc2)
    a[loc2].append(loc1)

k = 1
cvaz = [0] * (n + 1)

for i in range(1, n + 1):
    l = len(a[i])
    print(l + 1)
    print(i, k)
    k += 1
    cvaz[i] = k
    for j in range(l):
        if a[i][j] > i:
            print(i, k)
            k += 1
        else:
            print(i, cvaz[a[i][j]])
            cvaz[a[i][j]] += 1
