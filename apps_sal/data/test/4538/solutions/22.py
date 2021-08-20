(n, d) = map(int, input().split())
i = 1
a = 0
while i <= n:
    (x, y) = map(int, input().split())
    i += 1
    if x ** 2 + y ** 2 <= d ** 2:
        a += 1
print(a)
