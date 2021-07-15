n = 100001
p, t = [0]*n, [[] for i in range(n)]
t[1] = [1]
for i in range(2, n):
    t[i].append(i)
    for j in range(2*i, n, i):
        t[j].append(i)

n = input()
for i in map(int, input().split(" ")):
    x = max(p[j] for j in t[i]) + 1
    for j in t[i]:
        p[j] = x
print(max(p))

