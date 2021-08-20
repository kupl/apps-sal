n = int(input())
a = [int(i) for i in input().split()]
m = 1
c = 1
for i in range(1, n):
    if a[i] > a[i - 1]:
        c += 1
    else:
        m = max(m, c)
        c = 1
m = max(m, c)
print(m)
