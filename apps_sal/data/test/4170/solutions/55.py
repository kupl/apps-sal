n = int(input())
a = list(map(int, input().split()))
c = 0
d = 0
for i in range(n - 1):
    if a[i] >= a[i + 1]:
        c += 1
    else:
        c = 0
    d = max(c, d)
print(d)
