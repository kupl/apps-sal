(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
c = [0 for i in range(k)]
s = sum(a)
for i in range(n):
    c[i % k] += a[i]
ans = -1
for i in c:
    ans = max(ans, abs(s - i))
print(ans)
