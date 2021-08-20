N = int(input())
P = [int(x) for x in input().split()]
PIdx = sorted([(i + 1, v) for (i, v) in enumerate(P)], key=lambda x: x[1])
L = [0]
for i in range(N + 1):
    L.append(i)
R = [i + 1 for i in range(N + 1)]
R.append(N + 1)
ans = 0
for (i, v) in PIdx:
    l1 = L[i]
    l2 = L[l1]
    r1 = R[i]
    r2 = R[r1]
    ans += v * ((i - l1) * (r2 - r1) + (l1 - l2) * (r1 - i))
    L[r1] = l1
    R[l1] = r1
print(ans)
