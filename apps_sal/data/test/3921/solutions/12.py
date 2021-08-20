n = 111111
p = [0] * n
t = {}
t[1] = [1]
for i in range(2, n):
    if t.get(i, 0) == 0:
        t[i] = [i]
        for j in range(2 * i, n, i):
            if j not in t:
                t[j] = []
            t[j].append(i)
input()
a = list(map(int, input().split()))
for i in a:
    x = max((p[j] for j in t[i])) + 1
    for j in t[i]:
        p[j] = x
print(max(p))
