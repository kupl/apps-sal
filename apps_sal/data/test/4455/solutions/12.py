(n, k) = map(int, input().split())
a = list(map(int, input().split()))
rec = []
rec1 = {}
for i in range(n):
    rec.append((i, a[i]))
    rec1[i + 1] = a[i]
rec = sorted(rec, key=lambda s: s[1])
num = [0] * n
j = 0
for i in range(n):
    num[rec[i][0]] = i
i = 1
while i < n:
    if rec[i - 1][1] == rec[i][1]:
        j = 1
        while i < n and rec[i - 1][1] == rec[i][1]:
            num[rec[i][0]] -= j
            j += 1
            i += 1
    i += 1
for i in range(k):
    (x, y) = map(int, input().split())
    if rec1[x] < rec1[y]:
        num[y - 1] -= 1
    elif rec1[y] < rec1[x]:
        num[x - 1] -= 1
print(' '.join(map(str, num)))
