def R():
    return map(int, input().split())


(n, k) = R()
a = list(R())
l = []
m = 0
for i in range(n):
    if a[i] not in l:
        m += 1
        if len(l) < k:
            l.append(a[i])
        else:
            curmin = n
            curindex = 0
            found = [n] * len(l)
            for j in range(len(a[i + 1:])):
                if a[i + j + 1] in l and found[l.index(a[i + j + 1])] == n:
                    found[l.index(a[i + j + 1])] = j
            l[found.index(max(found))] = a[i]
print(m)
