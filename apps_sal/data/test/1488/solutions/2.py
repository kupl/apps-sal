def gcd(a, b): return a if b == 0 else gcd(b, a % b)


n = int(input())
l = sorted(map(int, input().split()))
t = sum((i + i - n + 1) * l[i] for i in range(n))
t = t + t + sum(l)
d = gcd(t, n)
print(t // d, n // d)
