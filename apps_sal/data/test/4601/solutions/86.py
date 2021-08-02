n, k = list(map(int, input().split()))
h = list(map(int, input().split()))
h.sort(reverse=True)

print((sum(h[k:])))
