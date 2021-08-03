def read(): return list(map(int, input().split()))


n, m = read()
v = list(read())

e = []
for i in range(m):
    x, y = [int(x) - 1 for x in input().split()]
    e.append((x, y, min(v[x], v[y])))
e.sort(key=lambda x: x[2], reverse=True)

belong = list(range(n))
union = [[i] for i in belong]
size = [1] * n

ans = 0

for i, j, k in e:
    fi, fj = belong[i], belong[j]
    if fi == fj:
        continue
    if not (len(union[fi]) > len(union[fj])):
        fi, fj = fj, fi
    ans += k * size[fi] * size[fj]
    size[fi] += size[fj]
    union[fi] += union[fj]
    for t in union[fj]:
        belong[t] = fi

print("%.7lf" % (ans * 2 / n / (n - 1)))
