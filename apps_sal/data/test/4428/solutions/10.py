n = int(input())
a = list(map(int, input().split()))
b = a[::-1]
sa = [0] * n
sb = [0] * n
sa[0] = a[0]
sb[0] = b[0]
for i in range(1, n):
    sa[i] = sa[i - 1] + a[i]
    sb[i] = sb[i - 1] + b[i]
i, j = 1, 1
rec = []
while i + j <= n:
    if sa[i - 1] == sb[j - 1]:
        rec.append(sa[i - 1])
        i += 1
    elif sa[i - 1] < sb[j - 1]:
        i += 1
    else:
        j += 1

if len(rec) == 0:
    print(0)
else:
    print(max(rec))
