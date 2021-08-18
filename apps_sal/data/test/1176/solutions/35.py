n = int(input())
a = list(map(int, input().split()))
c = 0
ab = 10**10
s = 0
for i in range(n):
    if a[i] < 0:
        c += 1
    if ab > abs(a[i]):
        ab = abs(a[i])
    s += abs(a[i])
if c % 2 == 0:
    print(s)
else:
    print((s - 2 * ab))
