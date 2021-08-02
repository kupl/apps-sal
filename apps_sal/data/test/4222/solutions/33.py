n, k = map(int, input().split())
d = []
a = []
for i in range(k):
    d.append(int(input()))
    a.append(list(map(int, input().split())))

a = sum(a, [])
count = 0
for i in range(n):
    if i + 1 in a:
        continue
    count += 1

print(count)
