n, m = map(int, input().split())
A = []
a = list(map(int, input().split()))
for i in range(n):
    A.append([a[i], 1])

l = []
for i in range(m):
    b, c = map(int, input().split())
    l.append([c, b])

A.extend(l)
A.sort()
A.reverse()
B = []

j = 0
cnt = -1
while cnt < n:
    B.extend([A[j][0]] * A[j][1])
    cnt = cnt + A[j][1]
    if cnt >= n:
        del B[n:]
    j = j + 1

print(sum(B))
