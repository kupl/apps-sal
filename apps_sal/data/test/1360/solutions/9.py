n = int(input())
d = []
for i in range(n):
    a, b = list(map(int, input().split()))
    d.append([a, b])
d.sort()
m = [c[0] for c in d]
m[0] = d[0][1]
for i in range(1, n):
    if m[i-1] <= d[i][1]:
        m[i] = d[i][1]
print(m[n-1])

    

    

