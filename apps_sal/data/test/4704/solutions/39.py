n = int(input())
a = list(map(int, input().split()))
s1 = sum(a)
s2 = 0
ans = 10**18
for i in range(n - 1):
    s1 -= a[i]
    s2 += a[i]
    ans = min(ans, abs(s1 - s2))
print(ans)
