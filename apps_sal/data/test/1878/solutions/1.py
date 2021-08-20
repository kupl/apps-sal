n = int(input())
s = 0
for i in range(n):
    (a, b, c, d) = list(map(int, input().split()))
    s += (c - a + 1) * (d - b + 1)
print(s)
