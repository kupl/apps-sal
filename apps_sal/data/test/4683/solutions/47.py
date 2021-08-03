n = int(input())
a = list(map(int, input().split()))
s = []
c = 0
ans = 0
for i in a:
    c += i
    s.append(c)
for i in range(n - 1):
    ans += (a[i] * (s[n - 1] - s[i])) % 1000000007
print(ans % 1000000007)
