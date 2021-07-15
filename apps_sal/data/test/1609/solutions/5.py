n = int(input())
a = input().split()
d = {}
for i in range(n):
    d[i+1] = 0
for i in range(n):
    a[i] = int(a[i])
    if not a[i] in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1
nls_pos = []
for i in range(n):
    if d[i+1] == 0:
        nls_pos.append(i+1)
for i in range(n):
    if d[a[i]] > 1 or a[i]>n:
        d[a[i]] -= 1
        a[i] = nls_pos[-1]
        nls_pos.pop()
for i in a:
    print(i, end=" ")
