n = int(input())
a = []
b = []
for i in range(n):
    (aa, bb) = list(map(int, input().split()))
    a.append(aa)
    b.append(bb)
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if a[j] == b[i]:
            a[j] = -1
count = 0
for i in range(n):
    if a[i] != -1:
        count += 1
print(count)
