(N, M) = map(int, input().split())
b = []
s = [0] * M
for i in range(N):
    a = list(map(int, input().split()))
    del a[0]
    a.sort()
    b.append(a)
for i in range(N):
    for j in range(len(b[i])):
        s[b[i][j] - 1] += 1
print(s.count(N))
