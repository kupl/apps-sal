n = int(input())
a = list(map(int, input().split()))
y = list()
for i in range(n):
    x = 0
    while a[i] % 2 == 0:
        a[i] /= 2
        x += 1
    y.append(x)
print(min(y))
