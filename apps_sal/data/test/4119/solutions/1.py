n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
t = 0
s = []
for i in range(m - 1):
    t += x[i + 1] - x[i]
    s.append(x[i + 1] - x[i])
s.sort(reverse=True)
for i in range(min(n - 1, m - 1)):
    t -= s[i]
print(t)
