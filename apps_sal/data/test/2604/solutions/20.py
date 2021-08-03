r, d = map(int, input().split())
n = int(input())
k = 0
for i in range(n):
    x, y, w = map(int, input().split())
    l = (x**2 + y**2)**(1 / 2)
    if l - w >= r - d and l + w <= r:
        k += 1
print(k)
