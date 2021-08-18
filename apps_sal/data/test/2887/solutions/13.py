n = int(input())
v = list(map(int, input().split()))
t = list(map(int, input().split()))
m = []
for i in range(n):
    s = 0
    for j in range(i + 1):
        e = v[j]
        v[j] = v[j] - t[i]
        if(v[j] < 0):
            v[j] = 0
        loss = e - v[j]
        s = s + loss
    m.append(s)
print(*m)
