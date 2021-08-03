n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [[int(i) for i in input().split()] for _ in range(m)]
a.sort()
b = sorted(b, key=lambda x: x[1], reverse=True)
d = []
j = 0
while (n <= len(a) or j < m):
    C = b[j][1]
    B = b[j][0]
    for i in range(B):
        d.append(C)
    j += 1
    if j >= m or len(d) > len(a):
        break

for i in range(min(len(d), len(a))):
    if a[i] < d[i]:
        a[i] = d[i]

print(sum(a))
