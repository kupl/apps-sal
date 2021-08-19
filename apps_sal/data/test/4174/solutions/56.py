(n, x) = map(int, input().split())
l = list(map(int, input().split()))
d = [0]
count = 0
for i in range(n):
    d.append(d[i] + l[i])
for c in d:
    if c <= x:
        count += 1
print(count)
