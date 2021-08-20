(n, k) = map(int, input().split())
h = [int(input()) for _ in range(n)]
l = []
h.sort()
for i in range(n + 1 - k):
    x = h[i + k - 1] - h[i]
    l.append(x)
print(min(l))
