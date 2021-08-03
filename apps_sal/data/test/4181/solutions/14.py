n = int(input())
a, b, c = [*map(int, input().split())], [*map(int, input().split())], 0
for i in range(n):
    d = min(a[i], b[i])
    c += d
    a[i] -= d
    b[i] -= d
    d = min(a[i + 1], b[i])
    c += d
    a[i + 1] -= d
print(c)
