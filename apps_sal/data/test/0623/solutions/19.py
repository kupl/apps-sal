n, m = [int(x) for x in input().split()]
k = 0
while max(n, m) > 1 and min(m, n) > 0:
    k += 1
    n, m = max(n, m) - 2, min(n, m) + 1
print(k)
