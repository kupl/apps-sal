(n, x) = list(map(int, input().split()))
m = []
for _ in range(n):
    m.append(int(input()))
a = 0
for i in m:
    x -= i
    a += 1
while x >= min(m):
    x -= min(m)
    a += 1
print(a)
