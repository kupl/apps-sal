n, m, k = map(int, input().split())
x, s = map(int, input().split())

a = [x] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
d = [0] + list(map(int, input().split()))

ab = list(zip(a, b))
ab.sort(key=lambda x: -x[1])

ans = x * n
ind = 0

for ai, bi in ab:
    while ind < k + 1 and d[ind] <= (s - bi): ind += 1
    if ind == 0: continue
    ans = min(ans, (n - c[ind - 1]) * ai)

print(ans)
