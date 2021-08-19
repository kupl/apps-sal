(n, k) = map(int, input().split())
h = [int(s) for s in input().split()]
ans = 0
h.sort(reverse=True)
if k >= n:
    ans = 0
else:
    ans = sum(h[k:n])
print(ans)
