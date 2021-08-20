N = int(input())
l = []
for _ in range(N):
    (A, B) = list(map(int, input().split()))
    l.append((A, B))
t = N // 2
tl = sorted(l)
tr = sorted(l, key=lambda x: -x[1])
if N % 2:
    print(tr[t][1] - tl[t][0] + 1)
else:
    (a1, a2) = (tl[t - 1][0], tr[t][1])
    (a3, a4) = (tl[t][0], tr[t - 1][1])
    print(a4 - a3 + a2 - a1 + 1)
