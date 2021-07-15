n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ns = 0
t = [-1] * k
for i in range(k):
    t[i] = [-1, -1]
u = 0
pr = 0
result = 0
z = 0
s = set()


def okr():
    return int(100 * pr / n + 0.5)

while pr != n:
    pr += z
    ns = okr()
    z = 0
    for i in range(k):
        if t[i] == [-1, -1]:
            if u != len(a):
                t[i] = [u, 1]
                if a[u] == 1:
                    if ns == 1:
                        if u not in s:
                            result += 1
                            s.add(u)
                    t[i] = [-1, -1]
                    z += 1
                u += 1
        else:
            t[i][1] += 1
            if t[i][1] == a[t[i][0]]:
                if t[i][1] == ns:
                    if t[i][0] not in s:
                        result += 1
                        s.add(t[i][0])
                t[i] = [-1, -1]
                z += 1
        if t[i] != [-1, -1] and t[i][1] == ns:
            if t[i][0] not in s:
                result += 1
                s.add(t[i][0])
print(result)

    
    

