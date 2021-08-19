n = int(input())
(l, r) = (0, 0)
for i in range(n):
    (x, y) = [int(x) for x in input().split()]
    l += x
    r += y
print(min(l, n - l) + min(r, n - r))
