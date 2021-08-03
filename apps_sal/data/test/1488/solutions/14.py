import fractions
x = int(input())
a = sorted(map(int, input().split()))
z = 2 * x + 1
ans = sum(((4 * i - z) * a[i - 1]) for i in range(1, x + 1, 1))
s = fractions._gcd(ans, x)
ans //= s
x //= s
ss = []
ss.append(ans)
ss.append(x)
print(*ss)
