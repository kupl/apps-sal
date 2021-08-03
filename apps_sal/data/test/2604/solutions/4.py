r, d = map(int, input().split())
r -= d
n = int(input())
k = 0
for _ in range(n):
    x, y, h = map(int, input().split())
    l = (x**2 + y**2)**(1 / 2)
    if l - h >= r and l + h <= r + d:
        k += 1
print(k)
