n = int(input())
a = sorted(list(map(int, input().split())))

x = sum(a[:n // 2])
y = sum(a[n // 2:])

print(x ** 2 + y ** 2)

