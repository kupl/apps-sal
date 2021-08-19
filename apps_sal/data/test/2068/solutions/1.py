n = int(input())
m = {'polycarp': 0}
for i in range(n):
    (s, r, t) = input().lower().split()
    m[s] = m[t] + 1
mx = 0
for y in list(m.values()):
    mx = max(mx, y)
print(mx + 1)
