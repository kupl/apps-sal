(n, x, y) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
for i in range(n):
    g1 = max(0, i - x)
    g2 = min(n - 1, i + y)
    if a[i] == min(a[g1:g2 + 1]):
        print(i + 1)
        break
