(x, k) = map(int, input().split())
r = [(x, x)]
for i in range(k):
    l = [int(x) for x in input().split()]
    r.append((l[1], l[2]) if l[0] == 1 else (l[1], l[1]))
r.sort()
(v1, v2, prev) = (0, 0, 0)
for cr in r:
    v1 += (cr[0] - prev) // 2
    v2 += cr[0] - prev - 1
    prev = cr[1]
print(v1, v2)
