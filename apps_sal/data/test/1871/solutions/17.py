(n, x) = list(map(int, input().split()))
c = list(map(int, input().split()))
t = 0
c.sort()
for i in range(n):
    t += x * c[i]
    x -= 1
    if x <= 0:
        x = 1
print(t)
