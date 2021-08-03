n = int(input())
h = list(map(int, input().split()))

c = h[0]
for i in range(1, n):
    if h[i] - h[i - 1] >= 0:
        c += h[i] - h[i - 1]

print(c)
