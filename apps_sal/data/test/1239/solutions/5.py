n = int(input())
a = sorted([int(i) for i in input().split()])
m = abs(a[1] - a[0])
count = 0
for i in range(1, len(a)):
    t = abs(a[i] - a[i - 1])
    if t < m:
        m = t
        count = 1
    elif t == m:
        count += 1
print(m, count)
