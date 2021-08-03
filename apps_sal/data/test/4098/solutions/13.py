def kk(): return map(int, input().split())
def ll(): return list(kk())


n, k = kk()
ls = sorted(ll())
vs, ne = [0] * n, [-1] * n
b = 0
for a in range(n):
    while b < n and ls[b] - ls[a] < 6:
        b += 1
    vs[a], ne[a] = b - a, b
curr = [0] * (n + 1)
# print(vs)
for _ in range(k):
    # print(curr)
    prev = curr
    curr = [0] * (n + 1)
    for i in range(n):
        curr[i] = vs[i] + prev[ne[i]]
    m = 0
    for i in range(n - 1, -1, -1):
        if m > curr[i]:
            curr[i] = m
        else:
            m = curr[i]
print(m)
