(n, m, x) = map(int, input().split())
l = 0
a = list(map(int, input().split()))
for j in a:
    l += 1 if j > x else 0
print(min(l, m - l))
