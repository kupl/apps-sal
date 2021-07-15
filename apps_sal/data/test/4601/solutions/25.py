n, k = map(int, input().split())
h = list(sorted(map(int, input().split())))
x = 0
if n > k:
    for i in range(n - k):
        x += h[i]

print(x)
