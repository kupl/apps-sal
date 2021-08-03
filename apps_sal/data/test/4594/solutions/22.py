n = int(input())
a = sorted([input() for i in range(n)])
c = 1
for i in range(n - 1):
    if a[i] < a[i + 1]:
        c += 1
print(c)
