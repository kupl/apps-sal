n, x, y = list(map(int, input().split()))
a = list(map(int, input().split()))

if x > y:
    print(n)
else:
    a.sort()
    i = 0
    while i < n and a[i] <= x:
        i += 1
    print(i // 2 + i % 2)

