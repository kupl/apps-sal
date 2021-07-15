n, m = list(map(int, input().split()))
s1 = {}
sn = []

for i in range(m):
    a, b = list(map(int, input().split()))
    if a == 1:
        s1[b] = 1
    elif b == n:
        sn.append(a)

res = False
for s in sn:
    if s in s1:
        res = True
        break

print("POSSIBLE" if res else "IMPOSSIBLE")
