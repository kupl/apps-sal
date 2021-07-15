n, m = list(map(int, input().split()))
a = sorted([int(x) for x in input().split()])
a.reverse()
s = 0
for x in a:
    s += x
print(("Yes" if a[m-1] >=  (s + 4 * m - 1) // (4 * m) else "No"))

