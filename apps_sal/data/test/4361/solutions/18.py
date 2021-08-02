n, k = map(int, input().split())
h = list(int(input()) for i in range(n))
h.sort()

c = []

for i in range(n - k + 1):
    a = h[i + k - 1] - h[i]
    c.append(a)

print(min(c))
