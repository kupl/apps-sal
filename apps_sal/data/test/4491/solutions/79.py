n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]

m = 0

for i in range(n):
    l = sum(a[0][:i + 1]) + sum(a[1][i:])
    m = max(m, l)

print(m)
