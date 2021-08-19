N = int(input())
A = list(map(int, input().split()))
d = dict()
for i in range(N):
    if A[i] not in d:
        d[A[i]] = 0
    d[A[i]] += 1
x = sum((x * (x - 1) // 2 for x in list(d.values())))
for i in range(N):
    y = d[A[i]]
    print(x - y * (y - 1) // 2 + (y - 1) * (y - 2) // 2)
