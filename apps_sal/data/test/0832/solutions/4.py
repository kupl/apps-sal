n = int(input())
a, b = [0] * n, [0] * n

for i in range(n):
    a[i], b[i] = list(map(int, input().split()))
s = 0
for j in a:
    s += b.count(j)
print(s)

