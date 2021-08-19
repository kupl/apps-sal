(n, x) = map(int, input().split())
l = list(map(int, input().split()))
a = 1
d = 0
for i in range(n):
    d += l[i]
    if d <= x:
        a += 1
print(a)
