n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
ans = 0

for i in range(m):
    ans -= a[b[i] - 1]
    c.append(a[b[i] - 1])
ans += sum(a)
c.sort()
c = c[::-1]
mx = ans
for i in range(m + 1):
    x = (sum(c[:i]) + ans) * (2 ** (m - i))
    if x > mx:
        mx = x
print(mx)
