n, p = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
s1, s2 = a[0], sum(a) - a[0]
ans = s1 % p + s2 % p
for i in range(n - 1):
    s1 = (s1 + a[i]) % p
    s2 = (s2 - a[i]) % p
    ans = max(ans, s1 + s2)
print(ans)
