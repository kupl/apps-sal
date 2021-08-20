n = int(input())
l = [0] * (n + 1)
for i in range(n - 1):
    (u, v) = input().split()
    (u, v) = [int(u), int(v)]
    l[u] += 1
    l[v] += 1
l = list(set(l))
if len(l) <= 2:
    print('YES')
elif l[2] == 2:
    print('NO')
else:
    print('YES')
