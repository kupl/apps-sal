(n, x) = map(int, input().split())
m = []
for _ in range(n):
    m.append(int(input()))
count = 0
x -= sum(m)
count += len(m)
while x >= min(m):
    x -= min(m)
    count += 1
print(count)
