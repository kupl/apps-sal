n = int(input())
a = input().split()
for i, x in enumerate(a):
    a[i] = int(x)

d = [float('inf')] * (n + 1)
d[0] = 0
length = 0
value = 0
s = dict()
for i in range(0, n):
    if a[i] - 1 in s:
        if a[i] is s:
            s[a[i]] = max(s[a[i]], s[a[i - 1]] + 1)
        else:
            s[a[i]] = s[a[i] - 1] + 1
    else:
        s[a[i]] = 1
    if s[a[i]] > length:
        length = s[a[i]]
        value = a[i]
ans = []
value0 = value - length + 1
for i, x in enumerate(a):
    if x == value0:
        ans.append(i + 1)
        value0 = value0 + 1
        if value0 > value:
            break

print(length)
print(' '.join(str(i) for i in ans))
