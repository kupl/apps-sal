n = int(input())
a = [0] + list(map(int, input().split())) + [0]
for i in range(int(input())):
    x, y = map(int, input().split())
    a[x - 1] += y - 1
    a[x + 1] += a[x] - y
    a[x] = 0
for i in range(1, n + 1):
    print(a[i])
