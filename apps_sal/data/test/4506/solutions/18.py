R = lambda: map(int, input().split())

m = 998244353
n = int(input())
a = list(R())
b = list(R())
for i in range(n): a[i] *= (i + 1) * (n - i)
a.sort()
b.sort(reverse=True)
print(sum([x * y % m for x, y in zip(a, b)]) % m)
