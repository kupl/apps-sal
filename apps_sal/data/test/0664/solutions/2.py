n = int(input())
a = list(map(int, input().split(' ')))
p = 0
for i in range(n - 1):
    if a[i] > a[i + 1]:
        p = i + 1
b = a[p:] + a[:p]
for i in range(n - 1):
    if b[i] > b[i + 1]:
        print(-1)
        break
else:
    print((n - p) % n)
