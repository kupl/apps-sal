n, k = list(map(int, input().split()))
h = list(map(int, input().split()))
h.sort(reverse=True)
h = h[k:]
print((sum(h)))
