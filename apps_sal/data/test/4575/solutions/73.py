n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]
a_eat = []
for i in range(n):
    y = 1
    j = 1
    while j + a[i] <= d:
        y += 1
        j += a[i]
    a_eat.append(y)

print(sum(a_eat) + x)
