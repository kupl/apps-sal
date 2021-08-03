n, t = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
p = 1
while p < t:
    p += a[p - 1]
if p == t:
    print("YES")
else:
    print("NO")
