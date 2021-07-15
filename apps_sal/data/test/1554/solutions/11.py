n = int(input())
a = list(map(int, input().split()))
z = []; p = set()
k1 = 1
for i in range(n):
    if a[i] in p:
        z.append((k1, i+1))
        k1 = i+2
        p = set()
    else:
        p.add(a[i])
if len(z) > 0:
    z[len(z)-1] = (z[len(z)-1][0], n)
    print(len(z))
    for k in z:
        print(k[0], k[1])
else:
    print(-1)

