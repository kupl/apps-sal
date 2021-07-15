n, t = int(input()), list(map(int, input().split()))
k = t.count(1)
t = [1 - 2 * i for i in t]

m, s = -1, 0

for i in range(n):
    s = max(s, 0)
    s += t[i]
    m = max(m, s)

print(k + m)
