n = int(input())
l = [0] * n
d = {}
d = [[]for _ in range(n)]
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    d[a - 1].append(b)
    d[b - 1].append(a)
l[0] = 1
check = [1]
while check:
    x = check.pop()
    for y in d[x - 1]:
        if not l[y - 1]:
            check.append(y)
            l[y - 1] = -1 * l[x - 1]
red = l.count(1)
print(red * (n - red) - n + 1)
