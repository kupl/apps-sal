n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

if k >= n:
    print(0)
else:
    h = h[:n - k]
    print(sum(h))
