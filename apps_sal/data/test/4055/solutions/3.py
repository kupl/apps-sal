n = int(input())
a = list(map(int, input().split()))
c1, c2 = 0, 0
for i in range(1, n - 1):
    if a[i - 1] == 1 and a[i] == 0 and a[i + 1] == 1:
        c1 += 1
for i in range(1, n - 1):
    if a[i - 1] == 1 and a[i] == 0 and a[i + 1] == 1:
        c2 += 1
        a[i + 1] = 0
print(min(c1, c2))
