n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

if k >= n:
    print(0)
else:
    # for i in range(k):
    # 	h.remove(max(h))
    h = h[:n - k]
    print(sum(h))
