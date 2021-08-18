n, m = list(map(int, input().split()))
q = [0] * (m)
w = [0] * (m)
for i in range(m):
    q[i], w[i] = [int(x) for x in input().split()]
w.sort(reverse=True)
s = 0
v = 0
for i in range(m):
    i = i + 1
    if (i % 2 == 1):
        v = i * (i - 1) // 2 + 1
    else:
        v = i * i // 2
    i = i - 1
    if(v > n):
        break
    s += w[i]
print(s)
