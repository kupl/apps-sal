n, m = map(int, input().split())
w = [0] + list(map(int, input().split()))
t, p = [], [0] * (n + 1)
s = 0
for i in map(int, input().split()):
    if p[i]:
        k = t.index(i)
        s += sum(w[j] for j in t[k + 1: ])
        t.append(t.pop(k))
    else:
        s += sum(w[j] for j in t)
        t.append(i)
        p[i] = 1
print(s)
