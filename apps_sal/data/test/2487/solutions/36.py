n = int(input())
a = 0
for i in range(n):
    a += (i + 1) * (n - i)
for _ in range(n - 1):
    (u, v) = map(int, input().split())
    if u > v:
        (u, v) = (v, u)
    a -= u * (n - v + 1)
print(a)
