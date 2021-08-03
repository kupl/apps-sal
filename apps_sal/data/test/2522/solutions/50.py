n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.reverse()
c = [0] * (n + 1)
for i in a:
    c[i] += 1
for i in b:
    c[i] += 1
if n < max(c):
    print('No')
    return
l = 0
while l < n and a[l] != b[l]:
    l += 1
i = 0
while l < n and a[l] == b[l]:
    while a[i] == b[l] or a[l] == b[i]:
        i += 1
    b[i], b[l] = b[l], b[i]
    l += 1
print('Yes')
print(' '.join([str(i) for i in b]))
