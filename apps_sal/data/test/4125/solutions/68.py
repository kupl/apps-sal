import fractions
(n, x) = list(map(int, input().split()))
l = list(map(int, input().split()))
l.append(x)
sl = sorted(l)
lis = [sl[i + 1] - sl[i] for i in range(n)]
ans = 0
for i in range(0, n):
    ans = fractions.gcd(ans, lis[i])
print(ans)
