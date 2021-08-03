n, k = map(int, input().split())
a = [int(i) for i in input().split()]
s = [0 for i in range(k)]
b = [a[0]]
for i in range(1, n):
    if a[i] == b[-1]:
        continue
    else:
        b.append(a[i])
y = len(b)
for i in range(y):
    if i == 0 and b[i] != b[i + 1]:
        s[a[0] - 1] += 1
    elif i == y - 1 and b[i] != b[i - 1]:
        s[b[y - 1] - 1] += 1
    else:
        if b[i - 1] == b[i + 1]:
            s[b[i] - 1] += 2
        else:
            s[b[i] - 1] += 1
x = max(s)
print(s.index(x) + 1)
