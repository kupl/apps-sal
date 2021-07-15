n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= 1
    if a[i] <= i + 1:
        a[i] = None

m = [-1] * n
m[0] = 0
now = [0]
next = []
while True:
    if not now:
        break
    for i in now:
        x = m[i] + 1
        if a[i] and m[a[i]] == -1:
            m[a[i]] = x
            next.append(a[i])
        if i != 0 and m[i - 1] == -1:
            m[i - 1] = x
            next.append(i - 1)
        if i != n - 1 and m[i + 1] == -1:
            m[i + 1] = x
            next.append(i + 1)
    now = next
    next = []

print(' '.join(map(str, m)))

