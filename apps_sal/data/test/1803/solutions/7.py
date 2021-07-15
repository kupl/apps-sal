3

n = int(input())
a = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    x, y = list(map(int, input().split()))
    if x > 1:
        a[x - 2] += y - 1
    if x < n:
        a[x] += a[x - 1] - y
    a[x - 1] = 0
print('\n'.join(map(str, a)))

