n = int(input())
l = list(map(int, input().split()))
r = []
s = 0
for i in range(n):
    s += l[i]
m = {}
for i in range(1000001):
    m[i] = 0
for i in range(n):
    m[l[i]] += 1
for i in range(n):
    cur = s - l[i]
    if cur // 2 > 1000000.0:
        continue
    if cur % 2 == 0:
        if cur // 2 == l[i]:
            if m[cur // 2] >= 2:
                r.append(i)
        elif m[cur // 2] > 0:
            r.append(i)
print(len(r))
for i in r:
    print(i + 1, end=' ')
