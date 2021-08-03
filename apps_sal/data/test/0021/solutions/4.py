n = int(input())
a = list(map(int, input().split()))
x = a.index(min(a))
y = a.index(max(a))

print(max(x, y, n - x - 1, n - y - 1))
