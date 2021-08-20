(n, k) = list(map(int, input().split()))
h = list(map(int, input().split()))
h.sort(reverse=True)
if k >= n:
    k = n
h2 = h[k:]
print(sum(h2))
