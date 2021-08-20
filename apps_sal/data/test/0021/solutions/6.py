n = int(input())
a = [int(x) for x in input().split()]
(c1, c2) = (-1, -1)
for i in range(n):
    if a[i] == 1:
        c1 = i
    if a[i] == n:
        c2 = i
print(max(abs(c1 - c2), c1, c2, n - 1 - c1, n - 1 - c2))
