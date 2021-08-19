n = int(input())
m = 0
for i in range(n):
    (a, b, c, d) = map(int, input().split())
    m += (c - a + 1) * (d - b + 1)
print(m)
