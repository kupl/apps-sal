# IAWT
n = int(input())
a = list(map(int, input().split()))
x = a.count(1)
y = a.count(2)
z = min(x, y)
x -= z
z += x // 3
print(z)
