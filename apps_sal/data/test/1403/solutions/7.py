n, k = list(map(int, input().split()))
x = list(map(int, input().split()))
x.sort()
y = 0
d = 0
for i in range(n - 1):
    if x[i + 1] > x[i] and x[i + 1] <= x[i] + k:
        y += 1 + d
        d = 0
    if x[i + 1] == x[i]:
        d += 1
    if x[i + 1] != x[i]:
        d = 0
print(n - y)
