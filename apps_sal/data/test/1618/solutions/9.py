n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = []
for _ in range(m):
    b.append(list(map(int, input().split())))
for (x, y) in b:
    m = max(a[0], a[x - 1])
    print(m)
    a[0] = m + y
