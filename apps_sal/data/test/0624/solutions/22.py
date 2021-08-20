(n, k, m) = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
s = sum(a)
ans = 0
while n > 0 and m > -1:
    s2 = (s + min(m, n * k)) / n
    ans = max(ans, s2)
    s -= a.pop()
    n -= 1
    m -= 1
print(ans)
