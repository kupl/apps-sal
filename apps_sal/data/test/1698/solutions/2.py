(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
prev = 1
ans = 0
for (i, x) in enumerate(a):
    t = n - i
    c = (t + k - 1) // k
    v = 2 * c * (x - prev)
    ans += v
    prev = x
print(ans)
