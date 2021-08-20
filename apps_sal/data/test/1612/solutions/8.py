n = int(input())
a = []
m = []
p = []
mn = []
for i in range(n):
    b = list(map(int, input().split()))
    a.insert(i, b)
    m.append(a[i][0])
    a[i] = a[i][1:]
    mn.append(set(a[i]))
    p.append('YES')
for j in range(n):
    for i in range(n):
        if i != j:
            if mn[i] <= mn[j]:
                p[j] = 'NO'
                break
for i in range(n):
    print(p[i])
