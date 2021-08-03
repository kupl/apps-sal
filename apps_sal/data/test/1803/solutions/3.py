n = int(input())
v = list(map(int, input().split()))
k = int(input())
for i in range(k):
    x, y = list(map(int, input().split()))
    x -= 1
    if x > 0:
        v[x - 1] += y - 1
    if x < n - 1:
        v[x + 1] += v[x] - y
    v[x] = 0

for x in v:
    print(x)
