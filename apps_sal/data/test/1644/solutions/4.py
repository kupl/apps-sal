t = [(9e9, 0, 0)]
n = int(input())
for i in range(n):
    a, b, h = map(int, input().split())
    t.append((b, a, h))
t.sort(reverse=True)
s, p = [0], [0] * (n + 1)
for i in range(1, n + 1):
    while t[s[-1]][1] >= t[i][0]: s.pop()
    p[i] = p[s[-1]] + t[i][2]
    s.append(i)
print(max(p))
