n,m = list(map(int, input().split()))
a = []
answ = []
for i in range(m):
    answ.append([])
for i in range(m):
    a.append([])
for i in range(m):
    a[i] = list(map(int, input().split()))
for i in range(m):
    v = a[i]
    mn = max(v)
    k = 0
    for j in reversed(list(range(n))):
        if a[i][j] == mn:
            k = j
    answ[i] = k
answ_k = []
for i in range(n):
    answ_k.append(0)
for i in range(len(answ)):
    answ_k[answ[i]] += 1
mn = max(answ_k)
for i in range(n):
    if answ_k[i] == mn:
        print(i+1)
        return

