(n, k) = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
s = 0
for i in range(n - k):
    s += h[i]
print(s)
