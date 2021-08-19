n = int(input())
a = list(map(int, input().split()))
l = [-1 for _ in range(n)]
for i in reversed(range(1, n + 1)):
    si = 0
    j = 2 * i - 1
    while j <= n - 1:
        si += l[j]
        j += i
    si = si % 2
    if si == 0:
        l[i - 1] = a[i - 1]
    elif a[i - 1] == 0:
        l[i - 1] = 1
    else:
        l[i - 1] = 0
b = []
for i in range(n):
    if l[i] == 1:
        b.append(i + 1)
print(len(b))
if len(b) != 0:
    print(*b)
