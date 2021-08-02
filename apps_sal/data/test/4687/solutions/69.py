n, k = map(int, input().split())
a = []
for i in range(n):
    A = list(map(int, input().split()))
    a.append(A)
a = sorted(a, key=lambda x: x[0])
b = 0
for i in range(n):
    b += a[i][1]
    if b >= k:
        print(a[i][0])
        return
